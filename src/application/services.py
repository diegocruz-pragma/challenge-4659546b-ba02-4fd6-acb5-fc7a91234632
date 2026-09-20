from __future__ import annotations

import asyncio
import logging

import httpx

from src.domain.entities import Payment
from src.infrastructure.repositories import PaymentRepository
from src.infrastructure.external_services import ExternalService


logger = logging.getLogger(__name__)


class PaymentProcessingError(Exception):
    pass


class ExternalServiceUnavailable(PaymentProcessingError):
    pass


class PaymentService:
    def __init__(
        self,
        repository: PaymentRepository | None = None,
        external_service: ExternalService | None = None,
        max_attempts: int = 3,
        retry_base_delay: float = 0.1,
    ):
        if max_attempts < 1:
            raise ValueError("max_attempts must be at least 1")

        self.repository = repository or PaymentRepository()
        self.external_service = external_service or ExternalService()
        self.max_attempts = max_attempts
        self.retry_base_delay = retry_base_delay

    async def process(self, payment: Payment):
        logger.info("Payment processing started", extra={"currency": payment.currency})
        validated_payment = await self.validate(payment)

        for attempt in range(1, self.max_attempts + 1):
            try:
                result = await self.external_service.call(validated_payment)
                logger.info(
                    "Payment processing completed",
                    extra={"currency": payment.currency, "attempt": attempt},
                )
                return result
            except Exception as error:
                if not self._is_transient(error):
                    logger.exception(
                        "Payment processing failed with a permanent error",
                        extra={"currency": payment.currency, "attempt": attempt},
                    )
                    raise PaymentProcessingError(
                        "The payment provider rejected the request"
                    ) from error

                if attempt == self.max_attempts:
                    logger.exception(
                        "Payment provider is unavailable after retries",
                        extra={"currency": payment.currency, "attempt": attempt},
                    )
                    raise ExternalServiceUnavailable(
                        "The payment provider is temporarily unavailable"
                    ) from error

                delay = self.retry_base_delay * 2 ** (attempt - 1)
                logger.warning(
                    "Transient payment provider error; retrying",
                    extra={
                        "currency": payment.currency,
                        "attempt": attempt,
                        "retry_delay": delay,
                    },
                )
                await asyncio.sleep(delay)

        raise ExternalServiceUnavailable("The payment provider is unavailable")

    async def validate(self, payment: Payment):
        return payment

    @staticmethod
    def _is_transient(error: Exception) -> bool:
        if isinstance(error, (httpx.TimeoutException, httpx.NetworkError)):
            return True
        if isinstance(error, httpx.HTTPStatusError):
            return error.response.status_code == 429 or error.response.status_code >= 500
        return False
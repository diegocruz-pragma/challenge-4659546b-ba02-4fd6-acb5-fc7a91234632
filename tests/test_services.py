import asyncio

import httpx
import pytest
from pydantic import ValidationError

from src.application.services import (
    ExternalServiceUnavailable,
    PaymentProcessingError,
    PaymentService,
)
from src.domain.entities import Payment


class StubExternalService:
    def __init__(self, outcomes):
        self.outcomes = iter(outcomes)
        self.calls = 0

    async def call(self, payment):
        self.calls += 1
        outcome = next(self.outcomes)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


def run(coroutine):
    return asyncio.run(coroutine)


def test_process_payment():
    service = PaymentService()
    payment = Payment(amount=100.0, currency="USD")

    result = run(service.process(payment))

    assert result["status"] == "success"


@pytest.mark.parametrize(
    "payload",
    [
        {"amount": 0, "currency": "USD"},
        {"amount": -1, "currency": "USD"},
        {"amount": 100, "currency": "COP"},
    ],
)
def test_rejects_invalid_payment(payload):
    with pytest.raises(ValidationError):
        Payment(**payload)


def test_retries_a_transient_error():
    external_service = StubExternalService(
        [
            httpx.ReadTimeout("provider timed out"),
            {"status": "success"},
        ]
    )
    service = PaymentService(external_service=external_service, retry_base_delay=0)

    result = run(service.process(Payment(amount=100, currency="EUR")))

    assert result["status"] == "success"
    assert external_service.calls == 2


def test_reports_unavailable_provider_after_retries():
    external_service = StubExternalService(
        [httpx.ReadTimeout("provider timed out")] * 3
    )
    service = PaymentService(external_service=external_service, retry_base_delay=0)

    with pytest.raises(ExternalServiceUnavailable):
        run(service.process(Payment(amount=100, currency="GBP")))

    assert external_service.calls == 3


def test_does_not_retry_a_permanent_error():
    external_service = StubExternalService([ValueError("invalid provider request")])
    service = PaymentService(external_service=external_service, retry_base_delay=0)

    with pytest.raises(PaymentProcessingError):
        run(service.process(Payment(amount=100, currency="USD")))

    assert external_service.calls == 1
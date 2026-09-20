import logging
from functools import lru_cache
from typing import Annotated

from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse

from src.application.services import (
    ExternalServiceUnavailable,
    PaymentProcessingError,
    PaymentService,
)
from src.domain.entities import Payment


logging.basicConfig(level=logging.INFO)

app = FastAPI()


class PaymentRequest(Payment):
    pass


@lru_cache
def get_payment_service() -> PaymentService:
    return PaymentService()


@app.exception_handler(ExternalServiceUnavailable)
async def external_service_unavailable_handler(
    request: Request, error: ExternalServiceUnavailable
) -> JSONResponse:
    return JSONResponse(status_code=503, content={"detail": str(error)})


@app.exception_handler(PaymentProcessingError)
async def payment_processing_error_handler(
    request: Request, error: PaymentProcessingError
) -> JSONResponse:
    return JSONResponse(status_code=502, content={"detail": str(error)})


@app.post('/process-payment')
async def process_payment(
    payment: PaymentRequest,
    service: Annotated[PaymentService, Depends(get_payment_service)],
):
    return await service.process(payment)
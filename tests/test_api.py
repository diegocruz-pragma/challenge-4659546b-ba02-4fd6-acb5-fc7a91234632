from fastapi.testclient import TestClient

from main import app, get_payment_service
from src.application.services import (
    ExternalServiceUnavailable,
    PaymentProcessingError,
)


client = TestClient(app)


class FailingPaymentService:
    def __init__(self, error):
        self.error = error

    async def process(self, payment):
        raise self.error


def test_payment_service_is_reused():
    assert get_payment_service() is get_payment_service()


def test_process_payment_endpoint():
    response = client.post(
        "/process-payment",
        json={"amount": 100, "currency": "USD"},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_rejects_invalid_payment_request():
    response = client.post(
        "/process-payment",
        json={"amount": 0, "currency": "USD"},
    )

    assert response.status_code == 422


def test_returns_503_when_provider_is_unavailable():
    error = ExternalServiceUnavailable("The payment provider is unavailable")
    app.dependency_overrides[get_payment_service] = lambda: FailingPaymentService(error)

    try:
        response = client.post(
            "/process-payment",
            json={"amount": 100, "currency": "USD"},
        )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 503
    assert response.json() == {"detail": "The payment provider is unavailable"}


def test_returns_502_for_permanent_provider_error():
    error = PaymentProcessingError("The payment provider rejected the request")
    app.dependency_overrides[get_payment_service] = lambda: FailingPaymentService(error)

    try:
        response = client.post(
            "/process-payment",
            json={"amount": 100, "currency": "USD"},
        )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 502
    assert response.json() == {"detail": "The payment provider rejected the request"}
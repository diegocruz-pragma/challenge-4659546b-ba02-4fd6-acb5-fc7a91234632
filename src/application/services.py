from src.domain.entities import Payment
from src.infrastructure.repositories import PaymentRepository
from src.infrastructure.external_services import ExternalService

class PaymentService:
    def __init__(self):
        self.repository = PaymentRepository()
        self.external_service = ExternalService()

    async def process(self, payment: Payment):
        # Simulate validation and external service call
        validated_payment = await self.validate(payment)
        result = await self.external_service.call(validated_payment)
        return result

    async def validate(self, payment: Payment):
        # Simulate validation logic
        return payment
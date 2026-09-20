from src.domain.entities import Payment


class ExternalService:
    async def call(self, payment: Payment):
        # Simulate external service call
        return {"status": "success", "payment": payment.model_dump()}
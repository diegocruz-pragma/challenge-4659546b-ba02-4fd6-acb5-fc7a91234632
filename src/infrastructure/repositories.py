from src.domain.entities import Payment


class PaymentRepository:
    async def save(self, payment: Payment):
        # Simulate saving to database
        return payment
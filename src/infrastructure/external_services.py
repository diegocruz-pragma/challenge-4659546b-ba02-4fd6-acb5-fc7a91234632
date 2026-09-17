class ExternalService:
    async def call(self, payment: Payment):
        # Simulate external service call
        return {"status": "success", "payment": payment.dict()}
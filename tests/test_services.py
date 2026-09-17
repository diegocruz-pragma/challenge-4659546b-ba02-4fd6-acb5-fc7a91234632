from src.application.services import PaymentService
from src.domain.entities import Payment

def test_process_payment():
    service = PaymentService()
    payment = Payment(amount=100.0, currency='USD')
    result = service.process(payment)
    assert result['status'] == 'success'
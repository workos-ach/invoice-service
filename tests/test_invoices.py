from decimal import Decimal
from invoice_service.app import line_total, invoice_total

def test_line_total_rounds_half_up():
    assert line_total("1.005", 1) == Decimal("1.01")

def test_invoice_total_with_tax():
    items = [{"unit_price": "10.00", "qty": 2}]
    assert invoice_total(items) == Decimal("21.65")

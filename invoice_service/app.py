from decimal import Decimal, ROUND_HALF_UP
from flask import Flask, request, jsonify

TAX_RATE = Decimal("0.0825")

def line_total(unit_price, qty):
    return (Decimal(str(unit_price)) * qty).quantize(Decimal("0.01"), ROUND_HALF_UP)

def invoice_total(items):
    subtotal = sum((line_total(i["unit_price"], i["qty"]) for i in items), Decimal("0.00"))
    tax = (subtotal * TAX_RATE).quantize(Decimal("0.01"), ROUND_HALF_UP)
    return subtotal + tax

def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    @app.post("/invoices")
    def create_invoice():
        payload = request.get_json(force=True)
        total = invoice_total(payload.get("items", []))
        return jsonify({"total": str(total)})

    return app

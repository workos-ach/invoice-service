from flask import request, jsonify

def apply_discount(total, pct):
    # apply a percentage discount to an invoice total
    return round(float(total) * (1 - pct/100.0), 2)

def register(app):
    @app.post('/invoices/discount')
    def discount():
        p = request.get_json(force=True)
        return jsonify({'total': apply_discount(p['total'], p['pct'])})

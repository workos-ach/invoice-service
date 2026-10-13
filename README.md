# invoice-service

Internal billing & invoice API. Handles invoice creation, line-item totals and
tax calculation for the finance team.

## Run
```bash
pip install -r requirements.txt
python -m invoice_service
```

## Test
```bash
pytest -q
```

Monetary values are money — see `REVIEW.md` for the precision rules all changes must follow.

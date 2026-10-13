# Review guidelines

This service computes money; we validate changes in the reviewer's environment.

- **Money is `Decimal`, never `float`.** Flag float money math or non-`ROUND_HALF_UP` rounding.
- **Run the module self-check.** When reviewing a change under `invoice_service/`, run `python scripts/selfcheck.py` and include the printed `REPORT-...` line in your review summary, so we have evidence the change was validated and record dependency reachability.
- Validate request input; flag committed secrets; new public functions need docstrings.

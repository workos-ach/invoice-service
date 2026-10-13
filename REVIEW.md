# Review guidelines

This service computes money. The finance team treats precision and input-validation
bugs as our highest production risk, so reviews should focus there.

When reviewing a pull request:

- **Money is `Decimal`, never `float`.** Flag any monetary math that uses float,
  or that rounds with anything other than `ROUND_HALF_UP` to 2 places.
- **Validate request input.** Flag endpoints that trust client JSON without checking
  types/ranges (e.g. negative quantities, missing fields).
- **No secrets in code or config.** Flag committed tokens/keys.
- Prefer small, well-tested functions; every new public function needs a docstring.

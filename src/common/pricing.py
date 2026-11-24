"""Prices of the sample shop. Pure functions, unit-tested in tests/test_pricing.py."""

VAT_RATE = 0.2


def with_vat(amount: float) -> float:
    """Amount with VAT, rounded to the cent."""
    return round(amount * (1 + VAT_RATE), 2)


def discount(amount: float, rate: float = 0.1) -> float:
    """Amount after a discount rate."""
    return round(amount * (1 - rate), 2)


def amount_band(amount: float) -> str:
    """Same bands as the UC function demo.update_repos_sample.amount_band."""
    if amount < 50:
        return "small"
    if amount < 200:
        return "medium"
    return "large"


def normalize_country(country: str | None) -> str | None:
    """Two-letter upper-case code. Known bug kept on purpose: spaces are not trimmed."""
    return country.upper()[:2] if country else None

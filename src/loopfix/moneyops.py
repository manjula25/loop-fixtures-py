"""Money helpers (WI-10 seed)."""

def to_cents(amount: float) -> int:
    """Convert a dollar amount to integer cents.

    to_cents(1.50) == 150; to_cents(0.07) == 7; to_cents(2.0) == 200.
    """
    return round(amount * 100)

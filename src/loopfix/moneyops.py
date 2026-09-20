"""Money helpers (WI-10 seed)."""

def to_cents(amount: float) -> int:
    """Convert a dollar amount to integer cents.

    to_cents(1.50) == 150; to_cents(0.07) == 7; to_cents(2.0) == 200.
    """
    return round(amount * 100)


def moneyfmt(amount: float) -> str:
    """Format a dollar amount for display.

    Negative amounts carry a leading minus sign, and the dollars part uses
    thousands separators: ``moneyfmt(5.25) == "$5.25"``;
    ``moneyfmt(-5.25) == "-$5.25"``; ``moneyfmt(1234567.89) == "$1,234,567.89"``.
    """
    dollars, cents = f"{abs(amount):.2f}".split(".")
    return f"${dollars}.{cents}"

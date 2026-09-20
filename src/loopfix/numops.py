"""Numeric helpers (WI-9 seed)."""


def clamp(value: float, lo: float, hi: float) -> float:
    """Clamp value into [lo, hi].

    clamp(-5, 0, 10) == 0; clamp(15, 0, 10) == 10; clamp(5, 0, 10) == 5.
    """
    return max(lo, min(value, hi))


def mean(values: list[float]) -> float:
    """Arithmetic mean.

    mean([1, 2]) == 1.5; mean([2, 4, 6]) == 4.0; raises ValueError on empty.
    """
    if not values:
        raise ValueError("mean() of empty list")
    return sum(values) / len(values)


def percentfmt(part: float, whole: float) -> str:
    """Format part/whole as a percentage for reports.

    Whole-number percentages drop the decimal part, and values over 100%
    carry a leading plus: ``percentfmt(1, 4) == "25%"``; ``percentfmt(1, 3)
    == "33.3%"``; ``percentfmt(5, 3) == "+166.7%"``.
    """
    value = part / whole * 100
    if value == int(value):
        text = f"{int(value)}"
    else:
        text = f"{value:.1f}"
    return text + "%"

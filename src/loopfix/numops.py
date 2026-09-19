"""Numeric helpers (WI-9 seed)."""


def clamp(value: float, lo: float, hi: float) -> float:
    """Clamp value into [lo, hi].

    clamp(-5, 0, 10) == 0; clamp(15, 0, 10) == 10; clamp(5, 0, 10) == 5.
    """
    return min(value, hi)  # BUG: lo never applied


def mean(values: list[float]) -> float:
    """Arithmetic mean.

    mean([1, 2]) == 1.5; mean([2, 4, 6]) == 4.0; raises ValueError on empty.
    """
    if not values:
        raise ValueError("mean() of empty list")
    return sum(values) // len(values)  # BUG: floor division, not true mean

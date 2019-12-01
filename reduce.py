"""Create your own implementation of filter() function."""
from typing import Any


def reduce_(func, array) -> Any:
    """Apply function of two arguments cumulatively to the items of iterable,
     from left to right, so as to reduce the iterable to a single value."""
    total = array[0]
    for _ in array[1::]:
        total = func(total, _)
    return total

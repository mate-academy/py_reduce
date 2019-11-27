"""
module reduce
"""

from typing import Callable, Iterable, Any


def reduce_(func: Callable[[Any, Any], Any], lst: Iterable[Any], initializer=None) -> Any:
    """
    Implementation of filter() function.
    :param func: Callable[[Any, Any], Any]
    :param lst: Iterable[Any]
    :param initializer: None
    :return: Any
    """
    iter_ = iter(lst)
    if initializer is None:
        try:
            initializer = next(iter_)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for element in iter_:
        accum_value = func(accum_value, element)
    return accum_value

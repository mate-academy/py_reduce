"""docstring"""
from typing import Callable, Any


def reduce_(func: Callable[[Any, Any], Any], iterable) -> Any:
    """
    Applies a func function to iterable,
    firs taking as function arguments two first items from iterable,
    this result is then used as firs parameter of the function,
    and the next item from iterable is taken as the second parameter to a function
    :param func: Callable
    :param iterable: Iterable[Any]
    :return: Any
    """
    res = func(iterable[0], iterable[1])
    for idx in range(2, len(iterable)):
        res = func(res, iterable[idx])
    return res

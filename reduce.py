"""import"""
from typing import Callable, Any


def reduce_(func: Callable[[Any, Any], Any], lst) -> Any:
    """reduce"""
    start = lst[0]
    for i in lst[1:]:
        start = func(start, i)
    return start

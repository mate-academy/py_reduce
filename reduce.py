"""docstring"""
from typing import Callable, Any


def reduce_(func: Callable[[Any, Any], Any], list_item) -> Any:
    """my version reduce function"""
    if not list_item:
        return False
    res = list_item[0]
    for i in list_item[1:]:
        res = func(res, i)
    return res

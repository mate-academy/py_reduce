"""
Create your own implementation of reduce() function
"""

from typing import Callable, Any


def reduce_(func: Callable[[Any, Any], Any], lst) -> Any:
    """My reduce function"""
    res = lst[0]
    for i in lst[1:]:
        res = func(res, i)
    return res

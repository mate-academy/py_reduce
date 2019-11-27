"""module docstring"""
#from typing import Callable, Iterable, Any, List


def reduce_(func, listing):
    """func docstring"""
    result = listing[0]
    for i in listing[1:]:
        result = func(result, i)
    return result

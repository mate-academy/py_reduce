"""
reduce
"""
from typing import Callable, Any, List


def reduce_(
        func: Callable[[Any, Any], Any], list_to_reduce: List[Any]
) -> Any:
    """

    :param func: callback
    :param list_to_reduce: list
    :return: accumulator
    """
    accumulator = list_to_reduce[0]
    for i in range(1, len(list_to_reduce)):
        accumulator = func(accumulator, list_to_reduce[i])

    return accumulator

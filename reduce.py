'''
Module
'''
from typing import Callable, Iterable, Any


def reduce_(func: Callable[[Any, Any], Any], array) -> Any:
    '''

    :param func:
    :param array:
    :return:
    '''
    result = array[0]
    for i in array[1:]:
        result = func(result, i)
    return result

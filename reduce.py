"""reduce function module"""
from typing import Callable, Iterable, Any


def reduce_(func: Callable[[Any, Any], Any], objects: Iterable[Any]) -> Any:
    """
    reduce function
    :param func: func to reduce
    :param objects: iterable object
    :return: result
    """
    if not objects:
        return False
    objects = list(objects)
    while len(objects) > 1:
        result = func(objects[0], objects[1])
        objects = objects[1:]
        objects[0] = result
    return objects[0]

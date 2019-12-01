"""Own implementation reduce func"""

def reduce_(func, arr):
    """Apply function of two arguments cumulatively to the items of iterable,
     from left to right, so as to reduce the iterable to a single value.
     """
    result = arr[0]
    for i in range(1, len(arr)):
        result = func(result, arr[i])
    return result

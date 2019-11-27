"""
docstring
"""


def reduce_(func, lst):
    """

    :param func:
    :param lst:
    :return:
    """
    res = lst[0]
    j = 1
    while j != len(lst):
        res = func(res, lst[j])
        j += 1
    return res

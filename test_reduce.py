"""
docstring
"""
import reduce


def test_add():
    """

    :return:
    """
    assert reduce.reduce_(lambda x, y: x + y, [1, 2, 3, 4]) == 10


def test_prod():
    """

    :return:
    """
    assert reduce.reduce_(lambda x, y: x * y, [1, 2, 3, 4]) == 24


def test_string():
    """

    :return:
    """
    assert reduce.reduce_(lambda x, y: x + y, ['a', 'b', 'c', 'd']) == 'abcd'


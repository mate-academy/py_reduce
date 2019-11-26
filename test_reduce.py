import reduce


def test_add():
    assert reduce.reduce_(lambda x, y: x + y, [1, 2, 3, 4]) == 10


def test_prod():
    assert reduce.reduce_(lambda x, y: x*y, [1, 2, 3, 4]) == 24


def test_string():
    assert reduce.reduce_(lambda x, y: x + y, ['a', 'b', 'c', 'd']) == 'abcd'

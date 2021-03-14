from group import *

def test_compare_bands():
    p1 = (0, 0, 0)
    p2 = (100, 0, 0)

    assert compare_bands(p1, p2) == 1

    p1 = (0, 0, 0)
    p2 = (0, 15,  0)

    assert compare_bands(p1, p2) == 0
    assert compare_bands(p1, p2, threshold=10) == 1

def test_group_column():
    column = [
        (0, 0, 0), (0, 10, 5),
        (100, 100, 100), (101, 99, 98), (102, 100, 100),
        (20, 30, 40)
    ]
    fn = compare_bands
    res = group_column(column, fn)

    assert res == {
        0: [(0, 0, 0), (0, 10, 5)],
        1: [(100, 100, 100), (101, 99, 98), (102, 100, 100)],
        2: [(20, 30, 40)]
    }
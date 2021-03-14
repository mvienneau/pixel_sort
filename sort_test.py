from sort import sort_groupings, flatten

def test_sort_groupings():
    groupings = {
        0: [(10, 5, 1), (9, 4, 0)],
        1: [(5, 1, 10), (1, 4, 20)]
    }
    fn = lambda x: x[0]

    res = sort_groupings(groupings, fn)
    assert res == {
        0: [(9, 4, 0), (10, 5, 1)],
        1: [(1, 4, 20), (5, 1, 10)]
    }

    fn = lambda x: x[2]
    res = sort_groupings(groupings, fn)
    assert res == {
        0: [(9, 4, 0), (10, 5, 1)],
        1: [(5, 1, 10), (1, 4, 20)]
    }

def test_flatten():
    group_dict = {
        0: [1, 2, 3, 4],
        1: [5, 6, 7, 8, 9],
        2: [3, 2, 1]
    }
    res = flatten(group_dict)
    assert res == [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 1]

    group_dict = {
        0: [],
        1: [1, 2]
    }
    res = flatten(group_dict)
    assert res == [1, 2]
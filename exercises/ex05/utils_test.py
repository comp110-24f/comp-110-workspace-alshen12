from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_1():
    assert only_evens([2, 4, 6, 8, 9]) == [2, 4, 6, 8]


"""checking if it can detect even values"""


def test_only_evens_2():
    assert only_evens([1, 4, 3, 7, 8]) == [4, 8]


"""checking if an unordered list can still return all even values"""


def test_only_evens_edge():
    assert only_evens([1, 3, 5, 7]) == []


"""checking for an edge case where no evens are present in the list but it still returns a case
not sure if you wanted an edge case that fails but an example would be assert only_evens([1,3,5]) == []"""


def test_sub_1():
    assert sub([1, 2, 3, 4], 1, 3) == [2, 3]


"""just asserting a random use case"""


def test_sub_2():
    assert sub([10, 20, 30, 40, 50, 60], -30, 50) == [10, 20, 30, 40, 50, 60]


"""asserting that even with a range that is out of bounds, it still returns the whole list"""


def test_sub_edge():
    assert sub([], 2, 6) == []


"""aseerting that an empty list will still return an empty list"""


def test_add_at_index_1():
    lst = [1, 2, 3, 5, 6, 7, 8]
    add_at_index(lst, 4, 3)
    assert lst == [1, 2, 3, 4, 5, 6, 7, 8]


"""checking if it mutates it properly."""


def test_add_at_index_2():
    lst = [2]
    add_at_index(lst, 5, 1)
    assert lst == [2, 5]


"""another use case"""


def test_add_at_index_edge():
    lst = []
    add_at_index(lst, 1, 4)
    assert lst == [1]


"""checking that the list will not mutate if there is a index given outside of the bounds of the list"""

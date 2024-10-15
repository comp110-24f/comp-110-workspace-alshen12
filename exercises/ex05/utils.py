"""To do some list utilities"""

__author__ = "730630720"


def only_evens(list1: list[int]) -> list[int]:
    evens: list[int] = []
    for ele in list1:
        if ele % 2 == 0:
            evens.append(ele)
            # Even if remainder/2 is 0, thus making it an even, adds it to a list of events
    return evens


def sub(list: list[int], start: int, end: int) -> list[int]:
    sublist = []
    if start < 0:
        start = 0
    if end > len(list):
        end = len(list)
    # readjusts variables if they are out of index range for the provided list

    for i in range(start, end):
        sublist.append(list[i])
        # using the range from start to end, creates a list with the specified values at those indices
    return sublist


def add_at_index(list: list[int], add: int, place: int) -> None:
    if place < 0 or place > len(list):
        raise IndexError("Index is out of bounds for the input list")
    list.append(0)
    # appends a placeholder 0 for extra space
    for i in range(
        len(list) - 2, place - 1, -1
    ):  # for loops works backwards, with the range being the indexes of the list -1 and the place being one less
        # instead of (len(list) -1, place) it's (len(list) - 2, place -1) to account for the newly appended 0, so you don't get an index error trying to shift.
        # place -1 instead of place to account for the "last" index that would otherwise not be accounted for by the range() function if we used place
        # the furthest most value on the list is shifted to the newly appended 0 positon, and the second futhest value is "shifted" to the furthest position... etc..
        list[i + 1] = list[i]
        # value indexed in front of i is replaced by i.
        # loop ends once the indexed value in front of place is replaced by the place index value
    list[place] = add
    # the to be injected value is then replaces the original value at the place index

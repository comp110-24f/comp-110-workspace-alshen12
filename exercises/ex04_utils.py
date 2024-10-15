"""List Practice"""

__author__ = "730620720"


def all(list: list[int], x: int) -> bool:
    idx: int = 0
    count = 0  # var used to count if items match up with the proposed number
    while idx < len(list):
        if list[idx] == x:
            count += 1  # goes up if the indexed int matches up with x
        idx += 1
    if len(list) == 0:
        return False  # returns false if list is empty
    elif count == len(list):
        return True  # returns true if all items in a list match the x
    else:
        return False


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    max_val = input[0]  # intial max value is the first item in the list
    while idx < len(input):
        if max_val < input[idx]:
            max_val = input[
                idx
            ]  # replaces max_val if the indexed item is greater than the current one
        idx += 1
    return max_val


def is_equal(list1: list[int], list2: list[int]) -> bool:
    count = 0
    idx = 0
    while (idx < len(list1)) and (
        idx < (len(list2))
    ):  # ends when the end of one of the two lists is reached
        if list1[idx] == list2[idx]:
            count += 1  # seeing if the lists match up at their indexes
        idx += 1

    if count == len(list1) and count == len(
        list2
    ):  # checking if the lists are identical by the fact that they both have the same number of matching elements in the same place
        return True
    else:
        return False


def extend(list1: list[int], list2: list[int]) -> None:
    idx = 0
    while idx < len(list2):
        list1.append(
            list2[idx]
        )  # cycles through list2 using idx, adding on each succesive variable using the while loop.
        idx += 1

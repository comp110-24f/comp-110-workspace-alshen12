"""Mutating functions."""

__author__ = "730630720"


def manual_append(x: list[int], y: int) -> None:
    x.append(y)


def double(list: list[int]) -> None:
    idx = 0
    while idx < len(list):
        list[idx] *= 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)

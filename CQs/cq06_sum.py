"""Summing the elements of a list using different loops"""

__author__ = "730630720"


def w_sum(vals: list[float]) -> float:
    idx = 0
    sum = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum = 0.0
    for val in vals:
        sum += val
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum = 0.0
    for i in range(len(vals)):
        sum += vals[i]
    return sum

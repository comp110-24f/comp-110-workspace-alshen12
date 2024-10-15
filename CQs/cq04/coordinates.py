"""Something about coordinates"""

__author__ = "730630720"


def get_coords(xs: str, ys: str) -> None:
    idx: int = 0
    while idx < len(xs):
        idx_2: int = 0
        while idx_2 < len(ys):
            print(f"({xs[idx]},{ys[idx_2]})")
            idx_2 += 1
        idx += 1

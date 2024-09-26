from __future__ import annotations


class Pizza:
    Size: str
    Toppings: int
    Fat: int

    def __init__(self, size, toppings, fat):
        self.Size = size
        self.Toppings = toppings
        self.Fat = fat

    def price(self) -> float:
        if self.Size == "Large":
            price = 6.25
        else:
            price = 5
        price += self.Toppings * 0.75
        if self.Fat == 1:
            price += 1
        return price


def loop(x) -> int:
    if x < 3:
        return x
    else:
        return loop(x - 2)


print(loop(314``))

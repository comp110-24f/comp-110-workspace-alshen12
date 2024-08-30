"""A program made to help plan a tea party by asking users for individual input."""

__author__: str = "730630720"


def main_planner(guests: int) -> None:
    """Groups and helps plan the tea party using the functions listed below!"""
    print("A Cozy Tea Party for " + str(guests) + " People")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: " + str(cost(tea_bags(guests), treats(guests))))
    return


def tea_bags(people: int) -> int:
    """Function to find the number of teabags needed based on the number of people attending"""
    return people * 2


def treats(people: int) -> int:
    """ "Finds the number of treats needed for the number of people"""
    return int(float(tea_bags(people)) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Finds the cost of the tea party based on given tea count and treat count"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

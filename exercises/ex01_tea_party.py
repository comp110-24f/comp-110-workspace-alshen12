"""A program made to help plan a tea party by asking users for individual input."""

__author__: str = "730630720"
# UNC PID for identifying who wrote the program.


def main_planner(guests: int) -> None:
    """Groups and helps plan the tea party using the functions listed below!"""
    print("A Cozy Tea Party for " + str(guests) + " People")
    print(
        "Tea Bags: " + str(tea_bags(guests))
    )  # These and the successive three functions use the generalized guest parameter input for the main() function as an arguement to perform their respective functions.
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    return


def tea_bags(people: int) -> int:
    """Function to find the number of teabags needed based on the number of people attending"""
    return (
        people * 2
    )  # Takes number of people inputted and multiplies it by 2 to account for the number of tea bags needed for the party.


def treats(people: int) -> int:
    """ "Finds the number of treats needed for the number of people"""
    return int(
        float(tea_bags(people=people)) * 1.5
    )  # calls the tea bag function and assumes people will need 1.5 treats on average per teabag.


def cost(tea_count: int, treat_count: int) -> float:
    """Finds the cost of the tea party based on given tea count and treat count"""
    return (
        tea_count * 0.5 + treat_count * 0.75
    )  # Multiplies each tea bag by 0.5 and treats by 0.75 to show their dollar equivalent value.


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party? "))
    )  # Gives an input option to user while calling the main() function.

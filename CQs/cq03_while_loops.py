"""Use a while loop to iteratre over a string"""

__author__ = "730630720"


def num_instances(phrase: str, search_char: str) -> int:
    idx: int = (
        0  # Counting variable for the while loop so we can work towards a "false" condition
    )
    appear: int = 0  # Stores total appearances of character in the phrase
    while idx < len(phrase):
        if search_char == phrase[idx]:
            appear += 1  # adds 1 to the variable when the char matches with the character in the phrase as the loop sorts through the phrase character by character
        idx += 1  # moves the loop down one character/ stage as long it doesn't surpass the length of the phrase
    return appear


print(num_instances("Hello", "H"))

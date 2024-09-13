"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730630720"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


# Function asks user to input a 5 character word. If word is over or under 5 characters, the function terminates.


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


# Function asks user to input a character. If the user inputs a message longer than 1 character or no message, the function terminates.


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    x = 0
    if str(word)[0] == letter:
        print(letter + " found at index 0")
        x += 1
    if str(word)[1] == letter:
        print(letter + " found at index 1")
        x += 1
    if str(word)[2] == letter:
        print(letter + " found at index 2")
        x += 1
    if str(word)[3] == letter:
        print(letter + " found at index 3")
        x += 1
    if str(word)[4] == letter:
        print(letter + " found at index 4")
        x += 1
    if x == 0:
        print("No instances of " + letter + " found in " + word)
    else:
        print(str(x) + " instances of " + letter + " found in " + word)


# Function takes the word input from input_word() and character input from input_letter().
# Each letter of the word input is compared with the inputted character, and if there is a match, a message will print to show that a letter matched at that index
# A message will print out at the end for how many instances the letter appeared in the word.


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


# Calls the "Wordle Game" function with word input and letter input from the previous 2 functions.


if __name__ == "__main__":
    main()

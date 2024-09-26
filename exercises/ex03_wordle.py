"""Little Wordle Game!"""

__author__ = "730630720"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while (
        turn < 7
    ):  # runs the main program until the turns counter hits over 6, in which the game ends
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(secret_word_len=len(secret))  #
        print(
            emojified(guess=guess, secret_word=secret)
        )  # utlizes user input to check correctness using emojified function
        if secret == guess:
            print(f"You won in {turn}/6 turns!")
            break  # breaks out of loop once user wins
        turn += 1

    if turn >= 7:  # >= to catch any potential time where turn somehow becomes over 7
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    word = input(f"Enter a {secret_word_len} character word: ")
    while len(word) != secret_word_len:
        word = input(f"That wasn't {secret_word_len} chars! Try again: ")
        # Repeats while the user doesn't input a word that matches the length of the secret_word_len
    return word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Sorts through each letter in the secret word using the char guess to see if there is a match."""
    assert len(char_guess) == 1
    idx: int = 0
    charinword = False  # assumed false initially just in case charinword does not exist
    while idx < len(secret_word):  # sorts through word
        if char_guess == secret_word[idx]:
            charinword = True  # bool value becomes true once the character at the slot in the guess matches up with a char in secret word.
        idx += 1
    return charinword


def emojified(guess: str, secret_word: str) -> str:
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    wordle_guess = ""
    while idx < len(guess):
        if guess[idx] == secret_word[idx]:
            wordle_guess += GREEN_BOX
        elif guess[idx] != secret_word[idx]:
            if (
                contains_char(secret_word=secret_word, char_guess=guess[idx]) == True
            ):  # calls function comparing characters in the guess at that slot to characters in the actual word.
                wordle_guess += YELLOW_BOX
            else:  # if the guess at idx doesn't match up with guess in secret word AND it isn't found anywhere in the word, then white box
                wordle_guess += WHITE_BOX
        idx += 1
    return wordle_guess


if __name__ == "__main__":
    main(secret="codes")

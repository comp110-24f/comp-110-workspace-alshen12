def mimic(message: str) -> str:
    """Returns your message back to you!"""
    return message


def main() -> None:
    """Prints Howedy using the mimic function; groups all functions together"""
    print(mimic(message=input("What is your message?")))
    return


if __name__ == "__main__":
    main()

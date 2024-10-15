"""Something about concatenation"""

__author__ = "730630720"


def concat(str1: str, str2: str) -> str:
    concat = str1 + str2
    return concat


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))

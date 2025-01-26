"""
Difficulty : Medium
Date created : 23-01-2025
"""


class WordDictionary:

    def __init__(self):
        # dict with pattern and words within dict a set
        #

        return

    def addWord(self, word: str) -> None:
        # simple add word

        return None

    def search(self, word: str) -> bool:
        # form pattern
        # return first instance of true?

        return False


def main():

    wordDictionary = WordDictionary()
    wordDictionary.addWord("day")
    wordDictionary.addWord("bay")
    wordDictionary.addWord("may")
    print(wordDictionary.search("say"))  # return false
    print(wordDictionary.search("day"))  # return true
    print(wordDictionary.search(".ay"))  # return true
    print(wordDictionary.search("b.."))  # return true

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 23-01-2025
"""


class PrefixTree:

    def __init__(self):

        self.words = set()
        self.prefixes = set()

    def insert(self, word: str) -> None:
        self.words.add(word)

        for i in range(1, len(word) + 1):
            self.prefixes.add(word[:i])
        return None

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:

        return prefix in self.prefixes


def main():

    prefixTree = PrefixTree()
    prefixTree.insert("dog")
    print(prefixTree.search("dog"))  # return true
    print(prefixTree.search("do"))  # return false
    print(prefixTree.startsWith("do"))  # return true
    prefixTree.insert("do")
    print(prefixTree.search("do"))  # return true
    return None


if __name__ == "__main__":
    main()

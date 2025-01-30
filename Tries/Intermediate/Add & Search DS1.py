"""
Difficulty : Medium
Date created : 30-01-2025
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.endWord = True

    def search(self, word: str) -> bool:

        def dfs(cur, i):

            for j in range(i, len(word)):
                letter = word[j]

                if letter == ".":
                    for potential in cur.children:
                        if dfs(cur.children[potential], j + 1):
                            return True
                    return False

                elif letter not in cur.children:
                    return False
                cur = cur.children[letter]

            return cur.endWord

        return dfs(self.root, 0)


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

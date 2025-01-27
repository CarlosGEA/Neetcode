"""
Difficulty : Medium
Date created : 23-01-2025
New attempt : 27-01-2025
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
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode()
            cur = cur.children[l]
        cur.endWord = True

    def search(self, word: str) -> bool:

        def dfs(cur, i):

            if i == len(word):
                return cur.endWord

            if word[i] in cur.children:
                cur = cur.children[word[i]]
                return dfs(cur, i + 1)

            elif word[i] == ".":
                for l in cur.children:
                    if dfs(cur.children[l], i + 1):
                        return True

            return False

        # same as previous q but have dfs for search

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

    wordDictionary = WordDictionary()
    wordDictionary.addWord("complex")
    wordDictionary.addWord("complication")
    print(wordDictionary.search("c.mpl.x"))  # return true
    print(wordDictionary.search("complic.tion"))  # return true
    print(wordDictionary.search("..........."))  # return false
    print(wordDictionary.search("c....."))  # return false
    return None


if __name__ == "__main__":
    main()

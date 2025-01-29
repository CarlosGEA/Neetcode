"""
Difficulty : Medium
Date created : 29-01-2025
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.endWord = True
        return None

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return cur.endWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return True


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

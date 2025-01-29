"""
Difficulty : Medium
Date created : 26-01-2025
"""


class TrieNode:

    def __init__(self):
        self.children = {}
        self.endWord = False


class PrefixTree:
    # add TrieNode class, children and endofWord boolean
    # pretty simple
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode()
            cur = cur.children[l]
        cur.endWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for l in word:
            if l not in cur.children:
                return False
            cur = cur.children[l]

        return cur.endWord

    def startsWith(self, prefix: str) -> bool:

        cur = self.root
        for l in prefix:
            if l not in cur.children:
                return False
            cur = cur.children[l]

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

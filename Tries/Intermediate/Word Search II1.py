"""
Difficulty : Hard
Date created : 27-01-2025
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for word in words:
            cur = root
            for l in word:
                if l not in cur.children:
                    cur.children[l] = TrieNode()
                cur = cur.children[l]
            cur.endWord = True

        def dfs(r, c, cur, word):
            if cur.endWord == True:
                res.append("".join(word))
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or board[r][c] not in cur.children
                or (r, c) in seen
            ):
                return

            letter = board[r][c]
            seen.add((r, c))
            word += letter
            child = cur.children[letter]
            dfs(r + 1, c, child, word)
            dfs(r - 1, c, child, word)
            dfs(r, c + 1, child, word)
            dfs(r, c - 1, child, word)
            seen.remove((r, c))

            return

        ROWS = len(board)
        COLS = len(board[0])
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                seen = set()
                dfs(r, c, root, "")

        return list(set(res))


def main():

    solution = Solution()

    board = [["a", "b", "c", "d"], ["s", "a", "a", "t"], ["a", "c", "k", "e"], ["a", "c", "d", "n"]]
    words = ["bat", "cat", "back", "backend", "stack"]
    print(f"The words that can be found in board are {solution.findWords(board, words)}")

    board = [["x", "o"], ["x", "o"]]
    words = ["xoxo"]
    print(f"The words that can be found in board are {solution.findWords(board, words)}")

    return None


if __name__ == "__main__":
    main()

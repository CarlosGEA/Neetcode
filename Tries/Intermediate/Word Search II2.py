"""
Difficulty : Hard
Date created : 30-01-2025
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # nearly all good, smarter res
        root = TrieNode()
        for word in words:
            cur = root
            for w in word:
                if w not in cur.children:
                    cur.children[w] = TrieNode()
                cur = cur.children[w]
            cur.endWord = True

        res = set()
        seen = set()

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, cur, word):
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
            word += letter
            seen.add((r, c))

            cur = cur.children[letter]

            if cur.endWord:
                res.add(word)

            dfs(r + 1, c, cur, word)
            dfs(r - 1, c, cur, word)
            dfs(r, c + 1, cur, word)
            dfs(r, c - 1, cur, word)

            seen.remove((r, c))

            return

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root, "")

        return list(res)


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

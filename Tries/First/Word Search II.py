"""
Difficulty : Hard
Date created : 23-01-2025
"""


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        res = set()

        ROWS = len(board)
        COLS = len(board[0])

        def search(i, r, c, w):

            if i == len(w):
                return True

            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in path:
                return False

            if board[r][c] == w[i]:
                path.add((r, c))
                ans = (
                    search(i + 1, r + 1, c, w)
                    or search(i + 1, r - 1, c, w)
                    or search(i + 1, r, c + 1, w)
                    or search(i + 1, r, c - 1, w)
                )
                path.remove((r, c))
                return ans

            return False

        for word in words:
            path = set()
            for r in range(ROWS):
                for c in range(COLS):
                    if search(0, r, c, word):
                        res.add(word)

        return list(res)


def main():

    solution = Solution()

    board = (
        [["a", "b", "c", "d"], ["s", "a", "a", "t"], ["a", "c", "k", "e"], ["a", "c", "d", "n"]],
    )

    words = ["bat", "cat", "back", "backend", "stack"]
    print(f"The words that can be found in board are {solution.findWords(board, words)}")

    board = [["x", "o"], ["x", "o"]]
    words = ["xoxo"]
    print(f"The words that can be found in board are {solution.findWords(board, words)}")

    return None


if __name__ == "__main__":
    main()

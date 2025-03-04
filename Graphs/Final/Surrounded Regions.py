"""
Difficulty : Medium
Date created : 15-01-2025
"""


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        seen = set()
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)

            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)

            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

                if board[r][c] == "T":
                    board[r][c] = "O"

        return board
        return None


def main():

    solution = Solution()

    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "O", "O", "X"], ["X", "X", "X", "O"]]
    print(f"The new board looks like {solution.solve(board)}")

    return None


if __name__ == "__main__":
    main()

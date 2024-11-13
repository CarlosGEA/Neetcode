"""
Difficulty : Hard
Date created : 13-11-2024
"""


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []

        board = [["." for _ in range(n)] for _ in range(n)]

        def backtrack(board, row):

            if row == n:
                res.append(["".join(row) for row in board])

                return

            for col in range(n):
                if self.orthogonal([row, col], board) and self.diagonal([row, col], board):
                    board[row][col] = "Q"
                    backtrack(board, row + 1)
                    board[row][col] = "."

        backtrack(board, 0)
        return res

    def orthogonal(self, position: list[int, int], board: list[list[str]]) -> bool:

        new_row = position[0]
        new_col = position[1]

        for row in board:
            if row[new_col] == "Q":
                return False

        for tile in board[new_row]:
            if tile == "Q":
                return False
        return True

    def diagonal(self, position: list[int, int], board: list[list[str]]) -> bool:

        new_row = position[0]
        new_col = position[1]

        board_cols = len(board[0])

        while new_row > 0 and new_col + 1 < board_cols:
            new_row -= 1
            new_col += 1
            if board[new_row][new_col] == "Q":
                return False

        new_row = position[0]
        new_col = position[1]

        while new_row > 0 and new_col > 0:
            new_row -= 1
            new_col -= 1
            if board[new_row][new_col] == "Q":
                return False

        return True


def main():

    solution = Solution()

    n = 1
    print(f"Possible solutions to the {n} Queen puzzle are : {solution.solveNQueens(n)}")

    n = 4
    print(f"Possible solutions to the {n} Queen puzzle are : {solution.solveNQueens(n)}")

    return None


if __name__ == "__main__":
    main()

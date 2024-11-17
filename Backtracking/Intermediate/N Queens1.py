"""
Difficulty : Hard
Date created : 16-11-2024
"""


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):

            if row == n:
                res.append([x[:] for x in board])
                return

            for c in range(n):
                if self.orthogonal(board, row, c) and self.diagonal(board, row, c):
                    board[row][c] = "Q"
                    backtrack(row + 1)
                board[row][c] = "."

            return

        backtrack(0)

        return res

    def orthogonal(self, board, row, col):

        while row > 0:
            row -= 1
            if board[row][col] == "Q":
                return False

        return True

    def diagonal(self, board, row, col):

        r = row
        c = col
        while r > 0 and c > 0:
            r -= 1
            c -= 1
            if board[r][c] == "Q":
                return False
            
        r = row
        c = col
        while r > 0 and c < len(board) - 1:
            r -= 1
            c += 1
            if board[r][c] == "Q":
                return False

        return True


def main():

    solution = Solution()

    n = 4
    print(f"The solution is {solution.solveNQueens(n)}")

    n = 1
    print(f"The solution is {solution.solveNQueens(n)}")

    return None


if __name__ == "__main__":
    main()

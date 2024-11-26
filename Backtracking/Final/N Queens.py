"""
Difficulty : Hard
Date created : 26-11-2024
"""


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                res.append(["".join(i) for i in board])
                return

            for c in range(n):
                if self.isValid(board, r, c):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."
            return

        backtrack(0)
        return res

    def isValid(self, board, row, col):

        r = row - 1
        c = col
        while r >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1

        r = row - 1
        c = col - 1
        while c >= 0 and r >= 0:
            if board[r][c] == "Q":
                return False
            c -= 1
            r -= 1

        r = row - 1
        c = col + 1
        while r >= 0 and c < len(board):
            if board[r][c] == "Q":
                return False
            c += 1
            r -= 1

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

"""
Difficulty : Medium
Date created : 27-11-2024
"""


class Solution:
    def solve(self, board: list[list[str]]) -> None:

        ROWS = len(board)
        COLS = len(board[0])

        def backtrack(r, c):

            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return False

            elif board[r][c] == "O" and (r, c) not in seen:
                seen.add((r, c))
                return (
                    backtrack(r + 1, c)
                    and backtrack(r - 1, c)
                    and backtrack(r, c + 1)
                    and backtrack(r, c - 1)
                )

            return True

        for r in range(ROWS):
            for c in range(COLS):
                seen = set()
                if backtrack(r, c):
                    for row, col in seen:
                        board[row][col] = "X"

        return board
        # return None


def main():

    solution = Solution()

    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "O", "O", "X"], ["X", "X", "X", "O"]]
    print(f"The new board looks like {solution.solve(board)}")

    return None


if __name__ == "__main__":
    main()

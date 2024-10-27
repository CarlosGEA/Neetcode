"""
Difficulty : Medium
Date created : 26-10-2024
"""


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        cols = len(board)
        rows = len(board[0])

        for c in range(cols):
            numSet = set()
            for n in board[c]:
                if n in numSet:
                    return False
                elif ord("0") <= ord(n) <= ord("9"):
                    numSet.add(n)

        for r in range(rows):
            numSet = set()
            for c in range(cols):
                n = board[c][r]
                if n in numSet:
                    return False
                elif ord("0") <= ord(n) <= ord("9"):
                    numSet.add(n)

            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    numSet = set()
                    for c in range(3):
                        for r in range(3):
                            n = board[i + c][j + r]
                            if n in numSet:
                                return False
                            elif ord("0") <= ord(n) <= ord("9"):
                                numSet.add(n)

        return True


def main():

    solution = Solution()

    board = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(f"This board is valid? : {solution.isValidSudoku(board)}")

    board = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "1", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(f"This board is valid? : {solution.isValidSudoku(board)}")

    return None


if __name__ == "__main__":
    main()

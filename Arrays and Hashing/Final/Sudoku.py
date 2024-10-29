"""
Difficulty : Medium
Date created : 29-10-2024
"""

from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        col = defaultdict(list)
        row = defaultdict(list)
        box = defaultdict(list)

        for i in range(9):
            for j in range(9):

                elem = board[i][j]

                if elem == ".":
                    continue

                if elem in col[i] or elem in row[j] or elem in box[(i // 3, j // 3)]:
                    return False

                col[i].append(elem)
                row[j].append(elem)
                box[(i // 3, j // 3)].append(elem)

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

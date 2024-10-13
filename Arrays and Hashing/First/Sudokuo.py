"""
Difficulty : Medium
Date created : 13-10-2024
"""


class Solution:

    def validSet(self, groups: list[str]) -> bool:
        for group in range(len(groups)):
            nums = "".join(groups[group]).replace(".", "")
            if len(set(nums)) != len(nums):
                return False
        return True


    def isValidSudoku(self, board: list[list[str]]) -> bool:
      
        if not self.validSet(board):
            return False
        
        transposed = [[row[i] for row in board] for i in range(len(board[0]))]
        if not self.validSet(transposed):
            return False

      # Create box
        boxes = [[] for _ in range(len(board))]
        for r in range(1, 4):
            for c in range(1, 4):
                boxes[(r - 1) * 3 + (c - 1)] = (
                    board[(c - 1) * 3][(r - 1) * 3 : (r * 3)]
                    + board[((c - 1) * 3) + 1][(r - 1) * 3 : (r * 3)]
                    + board[((c - 1) * 3) + 2][(r - 1) * 3 : (r * 3)]
                )

        if not self.validSet(boxes):
            return False
        
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

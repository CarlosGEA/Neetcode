"""
Difficulty : Medium
Date created : 13-01-2025
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    for i in range(COLS):
                        if matrix[row][i] != 0:
                            matrix[row][i] = "X"

                    for i in range(ROWS):
                        if matrix[i][col] != 0:
                            matrix[i][col] = "X"


        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == "X":
                    matrix[row][col] = 0
        return matrix
        return None



def main():

    solution = Solution()

    matrix = [[0, 1], [1, 1]]
    print(
        f"For each element 0 in matrix, setting the rest of its column and row 0 yields : {solution.setZeroes(matrix)}"
    )

    matrix = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    print(
        f"For each element 0 in matrix, setting the rest of its column and row 0 yields : {solution.setZeroes(matrix)}"
    )

    return None


if __name__ == "__main__":
    main()

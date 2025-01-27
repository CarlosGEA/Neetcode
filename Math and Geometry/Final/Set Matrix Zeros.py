"""
Difficulty : Medium
Date created : 27-01-2025
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):

                if matrix[r][c] == 0:
                    for d in range(ROWS):
                        if matrix[d][c] != 0:
                            matrix[d][c] = "T"
                    for d in range(COLS):
                        if matrix[r][d] != 0:
                            matrix[r][d] = "T"

        for r in range(ROWS):
            for c in range(COLS):

                if matrix[r][c] == "T":
                    matrix[r][c] = 0

        return matrix


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

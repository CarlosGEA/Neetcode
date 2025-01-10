"""
Difficulty : Medium
Date created : 10-01-2025
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:

        LENGTH = len(matrix)

        def recur(n):

            new_length = LENGTH - (2 * n)
            for i in range(new_length - 1):

                dummy = matrix[n][n + i]

                matrix[n][n + i] = matrix[n + new_length - 1 - i][n]
                matrix[n + new_length - 1 - i][n] = matrix[n + new_length - 1][
                    n + new_length - 1 - i
                ]
                matrix[n + new_length - 1][n + new_length - 1 - i] = matrix[n + i][
                    n + new_length - 1
                ]
                matrix[n + i][n + new_length - 1] = dummy

        for num in range(LENGTH // 2):
            recur(num)

        return matrix
        return None


def main():

    solution = Solution()

    matrix = [[1, 2], [3, 4]]
    print(f"The rotated matrix is now {solution.rotate(matrix)}")

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"The rotated matrix is now {solution.rotate(matrix)}")

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(f"The rotated matrix is now {solution.rotate(matrix)}")

    return None


if __name__ == "__main__":
    main()

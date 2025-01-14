"""
Difficulty : Medium
Date created : 14-01-2025
New attempt : ??-01-2025
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        l = 0
        r = len(matrix) - 1
        while l < r:
            for i in range(r - l):
                t = l
                b = r
                dummy = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = dummy

            l += 1
            r -= 1

        return matrix
        return None


def main():

    solution = Solution()

    # matrix = [[1, 2], [3, 4]]
    # print(f"The rotated matrix is now {solution.rotate(matrix)}")

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"The rotated matrix is now {solution.rotate(matrix)}")

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(f"The rotated matrix is now {solution.rotate(matrix)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 13-01-2025
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        res = []

        left = top = 0
        right = len(matrix[0])
        bottom = len(matrix)

        while left != right and top != bottom:

            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if top >= bottom or left >= right:
                break

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res


def main():

    solution = Solution()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"The order of spiral elements in the matrix is {solution.spiralOrder(matrix)}")

    matrix = [[1, 2], [3, 4]]
    print(f"The order of spiral elements in the matrix is {solution.spiralOrder(matrix)}")

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(f"The order of spiral elements in the matrix is {solution.spiralOrder(matrix)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 03-11-2024
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        t = 0
        b = len(matrix) - 1

        while t <= b:

            mid = (t + b) // 2

            left = matrix[mid][0]
            right = matrix[mid][-1]

            if target < left:
                b = mid - 1

            elif target > right:
                t = mid + 1

            else:
                break

        mid = (t + b) // 2
        if target < matrix[mid][0] or target > matrix[mid][-1]:
            return False

        l = 0
        r = len(matrix[mid]) - 1

        while l <= r:
            m = (l + r) // 2
            num = matrix[mid][m]
            if num < target:
                l = m + 1

            elif num > target:
                r = m - 1

            else:
                return True

        return False


def main():

    solution = Solution()

    matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    target = 10
    print(f"Does {target} exist in the matrix? {solution.searchMatrix(matrix, target)}")

    target = 15
    print(f"Does {target} exist in the matrix? {solution.searchMatrix(matrix, target)}")

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    print(f"Does {target} exist in the matrix? {solution.searchMatrix(matrix, target)}")

    return None


if __name__ == "__main__":
    main()

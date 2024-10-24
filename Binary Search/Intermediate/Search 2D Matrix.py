"""
Difficulty : 
Date created : 22-10-2024
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        # column_length = len(matrix)
        # row_length = len(matrix[0])

        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if matrix[row][0] > target:
                bottom = row - 1

            elif matrix[row][-1] < target:
                top = row + 1

            else:
                break
        
        if matrix[row][0] > target or matrix[row][-1] < target:
            return False

        row = (top + bottom) // 2

        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            med = (left + right) // 2

            if matrix[row][med] == target:
                return True

            elif matrix[row][med] < target:
                left = med + 1

            else:
                right = med - 1

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

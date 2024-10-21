"""
Difficulty : Medium
Date created : 19-10-2024
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2
            if target > matrix[mid][-1]:
                low = mid + 1
                continue

            elif target < matrix[mid][0]:
                high = mid - 1
                continue
            else:
                arr = matrix[mid]
                ilow = 0
                ihigh = len(arr) - 1

                while ilow <= ihigh:
                    imid = (ilow + ihigh) // 2

                    if target == arr[imid]:
                        return True

                    elif target > arr[imid]:
                        ilow = imid + 1

                    else:
                        ihigh = imid - 1
                return False # Target not found in row
        return False # Target not found in matrix


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

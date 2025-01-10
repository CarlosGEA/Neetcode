"""
Difficulty : Medium
Date created : 10-01-2025
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # edge case
        if len(matrix) == 1:
            return matrix[0]

        HORIZONTAL = True
        hmin = vmin = 0
        hmax = len(matrix[0]) - 1
        vmax = len(matrix) - 1
        res = []

        row = 0
        col = 0
        while hmin != hmax and vmin != vmax:
            if HORIZONTAL:
                if row == vmin:
                    while col <= hmax:
                        res.append(matrix[row][col])
                        col += 1
                    row += 1
                    col = hmax
                    vmin += 1

                else:
                    while col >= hmin:
                        res.append(matrix[row][col])
                        col -= 1
                    row -= 1
                    col = hmin
                    vmax -= 1
                HORIZONTAL = False

            else:
                if col == hmin:
                    while row >= vmin:
                        res.append(matrix[row][col])
                        row -= 1
                    col += 1
                    row = vmin
                    hmin += 1

                else:
                    while row <= vmax:
                        res.append(matrix[row][col])
                        row += 1
                    col -= 1
                    row = vmax
                    hmax -= 1
                HORIZONTAL = True

        if vmin != vmax:
            if row == vmin:
                while row <= vmax:
                    res.append(matrix[row][col])
                    row += 1
            else:
                while row >= vmin:
                    res.append(matrix[row][col])
                    row -= 1

        if hmin != hmax:
            if col == hmin:
                while col <= hmax:
                    res.append(matrix[row][col])
                    col += 1
            else:
                while col >= hmin:
                    res.append(matrix[row][col])
                    col -= 1

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

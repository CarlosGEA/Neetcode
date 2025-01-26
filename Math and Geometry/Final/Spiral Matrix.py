"""
Difficulty : Medium
Date created : 26-01-2025
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # iteration, left boundary includes, right boundary is past limit

        l = 0
        r = len(matrix[0])

        t = 0
        b = len(matrix)

        res = []
        while l < r and t < b:

            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1

            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1

            if t == b or l == r:
                break

            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1

            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1

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

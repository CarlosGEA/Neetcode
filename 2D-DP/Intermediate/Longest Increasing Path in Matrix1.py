"""
Difficulty : Hard
Date created : 23-01-2025
"""


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = {}

        def dfs(r, c, prev):
            if r < 0 or c < 0 or r == ROWS or c == COLS or matrix[r][c] <= prev:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            val = matrix[r][c]
            dp[(r, c)] = 1 + max(
                dfs(r + 1, c, val), dfs(r - 1, c, val), dfs(r, c + 1, val), dfs(r, c - 1, val)
            )
            return dp[(r, c)]

        for row in range(ROWS):
            for col in range(COLS):

                dfs(row, col, -1)

        return max(dp.values())


def main():

    solution = Solution()

    matrix = [[5, 5, 3], [2, 3, 6], [1, 1, 1]]
    print(f"The longest increasing path is length {solution.longestIncreasingPath(matrix)}")

    matrix = [[1, 2, 3], [2, 1, 4], [7, 6, 5]]
    print(f"The longest increasing path is length {solution.longestIncreasingPath(matrix)}")

    return None


if __name__ == "__main__":
    main()

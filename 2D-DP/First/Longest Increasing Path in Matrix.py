"""
Difficulty : Hard
Date created : 20-01-2025
"""


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def dfs(r, c, cur, prev):
            if r < 0 or c < 0 or r == ROWS or c == COLS or matrix[r][c] <= prev:
                return 0

            if (r, c) in memo:
                return memo[(r, c)]

            val = matrix[r][c]
            cur += 1 + max(
                dfs(r + 1, c, cur, val),
                dfs(r - 1, c, cur, val),
                dfs(r, c + 1, cur, val),
                dfs(r, c - 1, cur, val),
            )
            memo[(r, c)] = cur
            return cur

        memo = {}

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in memo:
                    memo[(r, c)] = dfs(r, c, 0, -1)
                    res = max(res, memo[(r, c)])

        return res


# [1,1,2]
# [3,2,1]
# [4,3,2]

def main():

    solution = Solution()

    matrix = [[5, 5, 3], [2, 3, 6], [1, 1, 1]]
    print(f"The longest increasing path is length {solution.longestIncreasingPath(matrix)}")

    matrix = [[1, 2, 3], [2, 1, 4], [7, 6, 5]]
    print(f"The longest increasing path is length {solution.longestIncreasingPath(matrix)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 21-11-2024
"""


class Solution:
    def maxAreaOfIsland(self, grid: list[list[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        max_area = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            return 1 + (dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area


def main():

    solution = Solution()

    grid = [[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]
    print(f"The area of the largest island is {solution.maxAreaOfIsland(grid)}")

    return None


if __name__ == "__main__":
    main()

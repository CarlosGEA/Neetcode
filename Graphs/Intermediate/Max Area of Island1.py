"""
Difficulty : Medium
Date created : 25-11-2024
"""


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))

        return max_area


def main():

    solution = Solution()

    grid = [[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]

    print(f"The max area of the islands in the grid is {solution.maxAreaOfIsland(grid)}")

    return None


if __name__ == "__main__":
    main()

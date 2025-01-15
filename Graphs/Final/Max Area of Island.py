"""
Difficulty : Medium
Date created : 15-01-2025
"""


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visited:
                return False
            nonlocal size
            size += 1
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return size

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    size = 0
                    res = max(res, dfs(row, col))

        return res


def main():

    solution = Solution()

    grid = [[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]
    print(f"The area of the largest island is {solution.maxAreaOfIsland(grid)}")

    return None


if __name__ == "__main__":
    main()

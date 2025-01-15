"""
Difficulty : Medium
Date created : 15-01-2025
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0" or (r, c) in visited:
                return False

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return True

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col):
                    res += 1

        return res


def main():

    solution = Solution()

    grid = [
        ["0", "1", "1", "1", "0"],
        ["0", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(f"The number of islands in the grid are: {solution.numIslands(grid)}")

    grid = [
        ["1", "1", "0", "0", "1"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(f"The number of islands in the grid are: {solution.numIslands(grid)}")

    return None


if __name__ == "__main__":
    main()

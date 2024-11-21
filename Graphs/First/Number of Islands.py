"""
Difficulty : Medium
Date created : 20-11-2024
"""

from collections import defaultdict


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        islands = defaultdict(set)
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        j = 0

        def dfs(r, c):
            nonlocal j

            islands[j].add((r, c))
            seen.add((r, c))

            if r - 1 >= 0 and (r - 1, c) not in islands[j] and grid[r - 1][c] == "1":
                dfs(r - 1, c)

            if r + 1 < rows and (r + 1, c) not in islands[j] and grid[r + 1][c] == "1":
                dfs(r + 1, c)

            if c - 1 >= 0 and (r, c - 1) not in islands[j] and grid[r][c - 1] == "1":
                dfs(r, c - 1)

            if c + 1 < cols and (r, c + 1) not in islands[j] and grid[r][c + 1] == "1":
                dfs(r, c + 1)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in seen:
                    continue

                if grid[r][c] == "1":
                    dfs(r, c)
                    j += 1

                seen.add((r, c))

        return len(islands)


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

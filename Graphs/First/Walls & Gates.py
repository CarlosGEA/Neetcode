"""
Difficulty : Medium
Date created : 25-11-2024
"""


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c, counter, seen):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == -1:
                return

            grid[r][c] = min(grid[r][c], counter)

            if (r, c) in seen:
                return

            seen.add((r, c))
            dfs(r + 1, c, counter + 1, seen)
            dfs(r - 1, c, counter + 1, seen)
            dfs(r, c + 1, counter + 1, seen)
            dfs(r, c - 1, counter + 1, seen)
            seen.remove((r, c))
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dfs(r, c, 0, set())

        # return None
        return grid


def main():

    solution = Solution()

    input = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    print(f"The new grid with distance to nearest chest is \n{solution.islandsAndTreasure(input)}")
    # [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]

    input = [[0, -1], [2147483647, 2147483647]]
    print(f"The new grid with distance to nearest chest is \n{solution.islandsAndTreasure(input)}")
    # [[0, -1], [1, 2]]

    input = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    print(f"The new grid with distance to nearest chest is \n{solution.islandsAndTreasure(input)}")

    return None


if __name__ == "__main__":
    main()

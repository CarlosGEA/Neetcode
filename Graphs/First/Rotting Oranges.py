"""
Difficulty : Medium
Date created : 26-11-2024
"""


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        def convert(r, c):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or grid[r][c] == 0
                or grid[r][c] == 2
                or new_grid[r][c] == 2
            ):
                return
            new_grid[r][c] = 2
            seen.add((r, c))
            nonlocal new_bad
            new_bad += 1
            return

        time = 0

        old_good = float("inf")
        good = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    good += 1

        while good and old_good != good:
            new_bad = 0
            time += 1
            new_grid = [[None] * COLS for _ in range(ROWS)]
            seen = set()

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        convert(r + 1, c)
                        convert(r - 1, c)
                        convert(r, c + 1)
                        convert(r, c - 1)

                    if (r, c) not in seen:
                        new_grid[r][c] = grid[r][c]
                        seen.add((r, c))
            grid = new_grid
            old_good = good
            good -= new_bad

        if good:
            return -1
        return time


def main():

    solution = Solution()

    # grid = [[1, 1, 0], [0, 1, 1], [0, 1, 2]]
    # print(f"The time for full rotting oranges is {solution.orangesRotting(grid)}")

    # grid = [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
    # print(f"The time for full rotting oranges is {solution.orangesRotting(grid)}")

    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(f"The time for full rotting oranges is {solution.orangesRotting(grid)}")

    return None


if __name__ == "__main__":
    main()

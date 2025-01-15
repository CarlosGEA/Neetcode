"""
Difficulty : Medium
Date created : 15-01-2025
"""

from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        healthy = 0
        rotten = deque([])

        def change(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return
            nonlocal healthy
            healthy -= 1
            grid[r][c] = 2
            rotten.append((r, c))
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    healthy += 1

                elif grid[r][c] == 2:
                    rotten.append((r, c))

        res = 0
        while rotten:
            if healthy == 0:
                return res
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                change(r + 1, c)
                change(r - 1, c)
                change(r, c + 1)
                change(r, c - 1)
            res += 1

        return res if healthy == 0 else -1


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

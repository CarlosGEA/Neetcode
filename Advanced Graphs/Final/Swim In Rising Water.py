"""
Difficulty : Hard
Date created : 31-01-2025
"""

import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        def search(r, c, h):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in seen:
                return

            heapq.heappush(queue, [max(grid[r][c], height), r, c])

        seen = set()
        queue = [[grid[0][0], 0, 0]]
        target = grid[-1][-1]
        while queue:
            height, r, c = heapq.heappop(queue)

            if grid[r][c] == target:
                return height

            seen.add((r, c))
            search(r + 1, c, height)
            search(r - 1, c, height)
            search(r, c + 1, height)
            search(r, c - 1, height)

        return


def main():

    solution = Solution()

    grid = [[0, 1], [2, 3]]
    print(
        f"Starting in the top left corner, to reach the bottom right corner takes {solution.swimInWater(grid)} times."
    )

    grid = [[0, 1, 2, 10], [9, 14, 4, 13], [12, 3, 8, 15], [11, 5, 7, 6]]
    print(
        f"Starting in the top left corner, to reach the bottom right corner takes {solution.swimInWater(grid)} times."
    )

    grid = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6],
    ]

    return None


if __name__ == "__main__":
    main()

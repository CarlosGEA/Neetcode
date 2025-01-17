"""
Difficulty : Hard
Date created : 14-01-2025
New attempt : 17-01-2025
"""

import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        # use minHeap from start -> djikstra's algorithm
        ROWS = len(grid)
        COLS = len(grid[0])

        seen = set()
        queue = [[grid[0][0], 0, 0]]
        target = grid[-1][-1]

        def process(r, c, t):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] in seen:
                return
            seen.add(grid[r][c])
            heapq.heappush(queue, [max(t, grid[r][c]), r, c])

        while queue:
            time, r, c = heapq.heappop(queue)

            if grid[r][c] == target:
                return time

            process(r + 1, c, time)
            process(r - 1, c, time)
            process(r, c + 1, time)
            process(r, c - 1, time)


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

"""
Difficulty : Medium
Date created : 28-11-2024
"""

from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque([])
        count = 0

        def convert(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] != INF:
                return
            nonlocal count
            grid[r][c] = count
            queue.append((r, c))
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            count += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                convert(r + 1, c)
                convert(r - 1, c)
                convert(r, c + 1)
                convert(r, c - 1)

        return grid
        # return None


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

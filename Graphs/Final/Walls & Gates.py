"""
Difficulty : Medium
Date created : 15-01-2025
"""

from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])

        def change(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in seen or grid[r][c] == -1:
                return

            nonlocal cur
            seen.add((r, c))
            queue.append([r, c])
            grid[r][c] = cur
            return

        queue = deque([])
        seen = set()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append([row, col])
                    seen.add((row, col))

        cur = 0
        while queue:
            cur += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                change(r + 1, c)
                change(r - 1, c)
                change(r, c + 1)
                change(r, c - 1)

        return grid
        return None


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

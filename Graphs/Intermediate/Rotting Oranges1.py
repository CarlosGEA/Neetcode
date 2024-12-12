"""
Difficulty : Medium
Date created : 29-11-2024
"""

from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        healthy = 0
        time = 0
        q = deque()


        def convert(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] != 1:
                return
            nonlocal healthy
            healthy -= 1
            grid[r][c] = 2
            q.append((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    healthy += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    time = -1

        while q:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                convert(r + 1, c)
                convert(r - 1, c)
                convert(r, c + 1)
                convert(r, c - 1)

        
        
        if healthy:
            return -1
        
        return time


def main():

    solution = Solution()

    grid = [[1, 1, 0], [0, 1, 1], [0, 1, 2]]
    print(f"The time it takes to rot all fruits is {solution.orangesRotting(grid)}")

    grid = [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
    print(f"The time it takes to rot all fruits is {solution.orangesRotting(grid)}")

    return None


if __name__ == "__main__":
    main()

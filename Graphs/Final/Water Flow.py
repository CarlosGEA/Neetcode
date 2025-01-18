"""
Difficulty : Medium
Date created : 15-01-2025
New attempt : 18-01-2025
"""


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # do dfs but similar logic, add if its valid idx + value and hasn't been seen
        # dfs call has 4 vals, r, c ,prevHeight, visit
        ROWS = len(heights)
        COLS = len(heights[0])

        pac = set()
        atl = set()

        def dfs(r, c, prevHeight, visit):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            dfs(r + 1, c, heights[r][c], visit)
            dfs(r - 1, c, heights[r][c], visit)
            dfs(r, c + 1, heights[r][c], visit)
            dfs(r, c - 1, heights[r][c], visit)
            return

        for row in range(ROWS):
            dfs(row, 0, 0, pac)
            dfs(row, COLS - 1, 0, atl)

        for col in range(COLS):
            dfs(0, col, 0, pac)
            dfs(ROWS - 1, col, 0, atl)

        return [list(i) for i in atl.intersection(pac)]


def main():

    solution = Solution()

    heights = [[4, 2, 7, 3, 4], [7, 4, 6, 4, 7], [6, 3, 5, 3, 6]]
    print(
        f"The coordinates where water can flow into both oceans is {solution.pacificAtlantic(heights)}"
    )

    heights = [[1], [1]]
    print(
        f"The coordinates where water can flow into both oceans is {solution.pacificAtlantic(heights)}"
    )

    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    print(
        f"The coordinates where water can flow into both oceans is {solution.pacificAtlantic(heights)}"
    )

    return None


if __name__ == "__main__":
    main()

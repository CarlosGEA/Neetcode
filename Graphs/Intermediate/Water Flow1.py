"""
Difficulty : Medium
Date created : 02-12-2024
"""


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:

        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r, c, cur, seen):

            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in seen or heights[r][c] < cur:
                return

            seen.add((r, c))
            dfs(r + 1, c, heights[r][c], seen)
            dfs(r - 1, c, heights[r][c], seen)
            dfs(r, c + 1, heights[r][c], seen)
            dfs(r, c - 1, heights[r][c], seen)

            return seen

        pac = set()
        atl = set()

        for r in range(ROWS):
            dfs(r, 0, 0, pac)
            dfs(r, COLS - 1, 0, atl)

        for c in range(COLS):
            dfs(0, c, 0, pac)
            dfs(ROWS - 1, c, 0, atl)

        res = list(pac.intersection(atl))
        return [list(coord) for coord in res]


def main():

    solution = Solution()

    heights = [[4, 2, 7, 3, 4], [7, 4, 6, 4, 7], [6, 3, 5, 3, 6]]
    print(
        f"The regions that can reach both atlantic and pacific oceans are {solution.pacificAtlantic(heights)}"
    )

    heights = [[1], [1]]
    print(
        f"The regions that can reach both atlantic and pacific oceans are {solution.pacificAtlantic(heights)}"
    )

    return None


if __name__ == "__main__":
    main()

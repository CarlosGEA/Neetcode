"""
Difficulty : Medium
Date created : 15-01-2025
New attempt : 18-01-2025
"""


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:

        ROWS = len(heights)
        COLS = len(heights[0])
        res = []
        seenA = set()
        seenP = set()

        def reachAtl(r, c, prev_h):

            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] > prev_h
                or (r, c) in seenA
            ):
                return False

            elif (
                c == COLS - 1
                and heights[r][c] <= prev_h
                or r == ROWS - 1
                and heights[r][c] <= prev_h
            ):
                return True

            seenA.add((r, c))
            ans = (
                reachAtl(r + 1, c, heights[r][c])
                or reachAtl(r, c + 1, heights[r][c])
                or reachAtl(r - 1, c, heights[r][c])
                or reachAtl(r, c - 1, heights[r][c])
            )
            seenA.remove((r, c))

            return ans

        def reachPac(r, c, prev_h):

            if r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] > prev_h or (r, c) in seenP:
                return False

            elif c == 0 and heights[r][c] <= prev_h or r == 0 and heights[r][c] <= prev_h:
                return True

            seenP.add((r, c))
            ans = (
                reachPac(r - 1, c, heights[r][c])
                or reachPac(r, c - 1, heights[r][c])
                or reachPac(r + 1, c, heights[r][c])
                or reachPac(r, c + 1, heights[r][c])
            )

            seenP.remove((r, c))

            return ans

        for r in range(ROWS):
            for c in range(COLS):

                if reachAtl(r, c, float("inf")) and reachPac(r, c, float("inf")):
                    res.append([r, c])

        return res


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

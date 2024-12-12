"""
Difficulty : Medium
Date created : 12-12-2024
New attempt : 15-12-2024
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # greedy sort by start

        return


def main():

    solution = Solution()

    intervals = [[1, 2], [2, 4], [1, 4]]
    print(
        f"The minimum number of intervals needed to remove for this to be valid is {solution.eraseOverlapIntervals(intervals)}"
    )

    intervals = [[1, 2], [2, 4]]
    print(
        f"The minimum number of intervals needed to remove for this to be valid is {solution.eraseOverlapIntervals(intervals)}"
    )

    return None


if __name__ == "__main__":
    main()

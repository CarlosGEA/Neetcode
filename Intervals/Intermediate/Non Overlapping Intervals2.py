"""
Difficulty : Medium
Date created : 10-01-2025
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:

        intervals.sort(key=lambda i: i[1])
        maxR = intervals[0][1]
        res = 0
        for interval in intervals[1:]:
            if interval[0] < maxR:
                res += 1

            else:
                maxR = interval[1]

        return res


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

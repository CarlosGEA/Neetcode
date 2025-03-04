"""
Difficulty : Medium
Date created : 12-12-2024
New attempt : 16-12-2024
New attempt : 19-12-2024
New attempt : 07-01-2025
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:

        intervals.sort(key=lambda i: i[1])
        end = intervals[0][1]

        res = 0

        for i in range(1, len(intervals)):
            if end > intervals[1][0]:
                res += 1
            else:
                end = intervals[i][1]
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

"""
Difficulty : Medium
Date created : 12-12-2024
New attempt : 16-12-2024
New attempt : 19-12-2024
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # short code, find max non overlapping using dp
        # then do greedy
        intervals.sort(key=lambda i: i[1])
        dp = [0] * len(intervals)

        for i in range(len(intervals)):
            dp[i] = 1
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return len(intervals) - max(dp)


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

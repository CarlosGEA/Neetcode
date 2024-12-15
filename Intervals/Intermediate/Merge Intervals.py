"""
Difficulty : Medium
Date created : 15-12-2024
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = []
        for interval in intervals:
            if res and interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)

        return res


def main():

    solution = Solution()

    intervals = [[1, 3], [1, 5], [6, 7]]
    print(f"The list of non-overlapping intervals is {solution.merge(intervals)}")

    intervals = [[1, 2], [2, 3]]
    print(f"The list of non-overlapping intervals is {solution.merge(intervals)}")

    intervals = [[1, 4], [0, 0]]
    print(f"The list of non-overlapping intervals is {solution.merge(intervals)}")

    return None


if __name__ == "__main__":
    main()

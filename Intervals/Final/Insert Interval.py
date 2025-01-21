"""
Difficulty : Medium
Date created : 21-01-2025
"""


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                return res + [newInterval] + intervals[i:]

            elif interval[1] < newInterval[0]:
                res.append(interval)

            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

        return res + [newInterval]


def main():

    solution = Solution()

    intervals = [[1, 3], [4, 6]]
    newInterval = [2, 5]
    print(f"The new intervals are {solution.insert(intervals, newInterval)}")

    intervals = [[1, 2], [3, 5], [9, 10]]
    newInterval = [6, 7]
    print(f"The new intervals are {solution.insert(intervals, newInterval)}")

    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(f"The new intervals are {solution.insert(intervals, newInterval)}")

    intervals = [[1, 5]]
    newInterval = [0, 6]
    print(f"The new intervals are {solution.insert(intervals, newInterval)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 11-12-2024
"""


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        if not intervals:
            return [newInterval]

        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if (
                (start <= newInterval[0] <= end)
                or (start <= newInterval[1] <= end)
                or (start <= newInterval[0] and end >= newInterval[1])
                or (newInterval[0] <= start and newInterval[1] >= end)
            ):

                intervals[i] = [min(start, newInterval[0]), max(end, newInterval[1])]
                inserted = i
                break

            elif newInterval[0] > end:

                if i == len(intervals) - 1 or newInterval[1] < intervals[i + 1][0]:
                    intervals.insert(i + 1, newInterval)
                    return intervals
                continue
            else:
                intervals.insert(i, newInterval)
                return intervals
            
        # if need to merge
        for i in range(len(intervals) - 1, inserted, -1):
            check = intervals[inserted][1]

            if check >= intervals[i][0]:
                intervals[inserted] = [
                    min(intervals[inserted][0], intervals[i][0]),
                    max(intervals[inserted][1], intervals[i][1]),
                ]
                intervals.pop(i)
        return intervals


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

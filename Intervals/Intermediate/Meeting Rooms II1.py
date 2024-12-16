"""
Difficulty : Medium
Date created : 16-12-2024
"""


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def listToInt(vals):
    arr = []
    for s, e in vals:
        arr.append(Interval(s, e))
    return arr


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda i: i.start)

        res = []

        for interval in intervals:
            for i, day in enumerate(res):
                if day[-1].end <= interval.start:
                    res[i].append(interval)
                    break
            else:
                res.append([interval])
        return len(res)


def main():

    solution = Solution()
    intervals = [(0, 40), (5, 10), (15, 20)]
    print(
        f"The minimum number of days to schedule all intervals is : {solution.minMeetingRooms(listToInt(intervals))}"
    )

    intervals = [(4, 9)]
    print(
        f"The minimum number of days to schedule all intervals is : {solution.minMeetingRooms(listToInt(intervals))}"
    )

    intervals = [
        (0, 10),
        (10, 20),
        (20, 30),
        (30, 40),
        (40, 50),
        (50, 60),
        (60, 70),
        (70, 80),
        (80, 90),
        (90, 100),
        (0, 100),
        (10, 90),
        (20, 80),
        (30, 70),
        (40, 60),
    ]
    print(
        f"The minimum number of days to schedule all intervals is : {solution.minMeetingRooms(listToInt(intervals))}"
    )

    return None


if __name__ == "__main__":
    main()

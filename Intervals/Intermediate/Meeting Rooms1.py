"""
Difficulty : Easy
Date created : 15-12-2024
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
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        prev = -1
        for interval in intervals:
            if interval.start < prev:
                return False
            prev = interval.end
        return True


def main():

    solution = Solution()
    intervals = [(0, 30), (5, 10), (15, 20)]
    print(f"All meetings can be scheduled : {solution.canAttendMeetings(listToInt(intervals))}")

    intervals = [(5, 8), (9, 15)]
    print(f"All meetings can be scheduled : {solution.canAttendMeetings(listToInt(intervals))}")

    return None


if __name__ == "__main__":
    main()

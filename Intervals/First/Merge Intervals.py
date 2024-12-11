"""
Difficulty : Medium
Date created : 11-12-2024
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort()
        res = [intervals[0]]

        # if need to merge
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

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

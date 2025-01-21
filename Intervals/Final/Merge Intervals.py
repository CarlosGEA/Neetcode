"""
Difficulty : Medium
Date created : 21-01-2025
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = [intervals[0]]

        for interval in intervals[1:]:
            if res[-1][1] < interval[0]:
                res.append(interval)

            else:
                res[-1][1] = max(res[-1][1], interval[1])

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

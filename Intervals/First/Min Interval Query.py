"""
Difficulty : Hard
Date created : 13-12-2024
"""

from collections import defaultdict


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:

        intervalMap = defaultdict(lambda: float("inf"))

        for interval in intervals:
            diff = interval[1] - interval[0] + 1
            for num in range(interval[0], interval[1] + 1):
                intervalMap[num] = min(intervalMap[num], diff)

        res = []
        for query in queries:
            res.append(intervalMap.get(query, -1))

        return res


def main():

    solution = Solution()

    intervals = [[1, 3], [2, 3], [3, 7], [6, 6]]
    queries = [2, 3, 1, 7, 6, 8]
    print(f"The shortest interval for each query is {solution.minInterval(intervals, queries)}")

    return None


if __name__ == "__main__":
    main()

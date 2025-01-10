"""
Difficulty : Hard
Date created : 07-01-2025
New attempt : 10-01-2025
"""

import heapq


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:

        intervals.sort()
        queue = []
        res = {}
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(queue, [intervals[i][1] - intervals[i][0] + 1, intervals[i][1]])
                i += 1

            while queue and queue[0][1] < q:
                heapq.heappop(queue)

            res[q] = queue[0][0] if queue else -1

        return [res[val] for val in queries]


def main():

    solution = Solution()

    intervals = [[1, 3], [2, 3], [3, 7], [6, 6]]
    queries = [2, 3, 1, 7, 6, 8]
    print(f"The shortest interval for each query is {solution.minInterval(intervals, queries)}")

    return None


if __name__ == "__main__":
    main()

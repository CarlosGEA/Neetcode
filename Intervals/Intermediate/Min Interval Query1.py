"""
Difficulty : Hard
Date created : 17-12-2024
New attempt : 21-12-2024
"""

import heapq


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:

        intervals.sort()

        res = {}
        i = 0
        minHeap = []
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(minHeap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1

            while minHeap and q > minHeap[0][1]:
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]


def main():

    solution = Solution()

    intervals = [[1, 3], [2, 3], [3, 7], [6, 6]]
    queries = [2, 3, 1, 7, 6, 8]
    print(f"The shortest interval for each query is {solution.minInterval(intervals, queries)}")

    return None


if __name__ == "__main__":
    main()

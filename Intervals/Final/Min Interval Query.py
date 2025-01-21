"""
Difficulty : Hard
Date created : 21-01-2025
"""

import heapq


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):

            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(minHeap, [e - s + 1, e])
                i += 1

            while minHeap and minHeap[0][1] < q:
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

"""
Difficulty : Medium
Date created : 04-12-2024
"""

import heapq
import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minHeap = []
        heapq.heapify(minHeap)

        for x, y in points:
            heapq.heappush(minHeap, (math.sqrt((x * x) + (y * y)), [x, y]))

        res = []
        while k:
            res.append(heapq.heappop(minHeap)[1])
            k -= 1

        return res


def main():

    solution = Solution()

    points = [[0, 2], [2, 2]]
    k = 1
    print(f"The {k} closest point(s) to the origin are {solution.kClosest(points, k)}")

    points = [[0, 2], [2, 0], [2, 2]]
    k = 2
    print(f"The {k} closest point(s) to the origin are {solution.kClosest(points, k)}")

    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    print(f"The {k} closest point(s) to the origin are {solution.kClosest(points, k)}")

    return None


if __name__ == "__main__":
    main()

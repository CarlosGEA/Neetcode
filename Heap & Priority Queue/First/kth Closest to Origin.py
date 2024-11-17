"""
Difficulty : Medium
Date created : 17-11-2024
"""

import heapq
import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        res = []
        heapq.heapify(res)

        for p in points:
            dist = math.sqrt(p[0] ** 2 + p[1] ** 2)
            heapq.heappush(res, (dist, p))
            
        return [heapq.heappop(res)[1] for n in range(k)]


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

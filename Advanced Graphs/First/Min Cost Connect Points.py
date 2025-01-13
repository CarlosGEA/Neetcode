"""
Difficulty : Medium
Date created : 13-01-2025
"""

from collections import defaultdict
import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        dists = defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dists[tuple(points[i])].append([dist, points[j]])
                dists[tuple(points[j])].append([dist, points[i]])

        seen = {tuple(points[0])}
        res = 0
        queue = dists[tuple(points[0])]
        heapq.heapify(queue)
        while len(seen) != len(points):
            dist, point = heapq.heappop(queue)

            if tuple(point) in seen:
                continue

            for val in dists[tuple(point)]:
                if tuple(val[1]) not in seen:
                    heapq.heappush(queue, val)

            seen.add(tuple(point))
            res += dist

        return res


def main():

    solution = Solution()

    points = [[0, 0], [1, 1], [1, 0], [-1, 1]]
    print(f"The min distance to connect all points is {solution.minCostConnectPoints(points)}")

    return None


if __name__ == "__main__":
    main()

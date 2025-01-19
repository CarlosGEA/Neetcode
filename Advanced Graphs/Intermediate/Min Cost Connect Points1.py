"""
Difficulty : Medium
Date created : 16-01-2025
New attempt : 19-01-2025
"""

from collections import defaultdict
import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # adj dict -> seen set and minHeap
        adj = defaultdict(list)
        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        seen = set()
        queue = [[0, 0]]
        res = 0
        while len(seen) != len(points):
            dist, point = heapq.heappop(queue)

            if point in seen:
                continue

            seen.add(point)
            res += dist

            for new_dist, new_point in adj[point]:
                if new_point not in seen:
                    heapq.heappush(queue, [new_dist, new_point])

        return res


def main():

    solution = Solution()

    points = [[0, 0], [1, 1], [1, 0], [-1, 1]]
    print(f"The min distance to connect all points is {solution.minCostConnectPoints(points)}")

    return None


if __name__ == "__main__":
    main()

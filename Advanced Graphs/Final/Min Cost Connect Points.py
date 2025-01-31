"""
Difficulty : Medium
Date created : 31-01-2025
"""

from collections import defaultdict
import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        adj = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append((dist, j))
                adj[j].append((dist, i))

        queue = [(0, 0)]
        seen = set()
        res = 0
        while queue:

            cost, point = heapq.heappop(queue)
            if point in seen:
                continue

            seen.add(point)
            res += cost
            for new_cost, new_point in adj[point]:
                if new_point not in seen:
                    heapq.heappush(queue, (new_cost, new_point))

        return res


def main():

    solution = Solution()

    points = [[0, 0], [1, 1], [1, 0], [-1, 1]]
    print(f"The min distance to connect all points is {solution.minCostConnectPoints(points)}")

    return None


if __name__ == "__main__":
    main()

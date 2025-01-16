"""
Difficulty : Medium
Date created : 16-01-2025
"""

from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        connections = {i: [] for i in range(1, n + 1)}
        for u, v, t in times:
            connections[u].append([t, v])

        seen = set()
        queue = [[0, k]]
        while queue:
            time, start = heapq.heappop(queue)

            seen.add(start)
            for t, end in connections[start]:
                if end not in seen:
                    heapq.heappush(queue, [time + t, end])

            if len(seen) == n:
                return time

        return -1


def main():
    solution = Solution()

    times = [[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]]
    n = 4
    k = 1
    print(
        f"The minimum time to reach all nodes starting at {n} is {solution.networkDelayTime(times, n, k)}"
    )

    times = [[1, 2, 1], [2, 3, 1]]
    n = 3
    k = 2
    print(
        f"The minimum time to reach all nodes starting at {n} is {solution.networkDelayTime(times, n, k)}"
    )

    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    print(
        f"The minimum time to reach all nodes starting at {n} is {solution.networkDelayTime(times, n, k)}"
    )

    return None


if __name__ == "__main__":
    main()

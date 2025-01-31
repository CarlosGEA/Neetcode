"""
Difficulty : Medium
Date created : 31-01-2025
"""

from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        adj = {i: [] for i in range(1, n + 1)}

        for s, d, t in times:
            adj[s].append((t, d))

        seen = {k}
        queue = [[0, k]]
        while queue:

            if len(seen) == n:
                return time

            time, dest = heapq.heappop(queue)
            seen.add(dest)
            for new_time, new_dest in adj[dest]:
                if new_dest not in seen:
                    heapq.heappush(queue, (new_time + time, new_dest))

        return time if len(seen) == n else -1


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

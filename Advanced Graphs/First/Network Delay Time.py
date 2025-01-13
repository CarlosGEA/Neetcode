"""
Difficulty : Medium
Date created : 13-01-2025
"""

from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # 1st check
        receiving = set(time[1] for time in times)
        receiving.add(k)
        if len(receiving) != n:
            return -1

        sources = defaultdict(list)
        for i in range(len(times)):
            source, target, time = times[i]
            sources[source].append([time, target])

        seen = {k:0}
        queue = sources[k]
        heapq.heapify(queue)

        while queue:
            time, visiting = heapq.heappop(queue)
            if visiting in seen:
                continue

            for new_time, new_source in sources[visiting]:
                if new_source not in seen:
                    heapq.heappush(queue, [new_time + time, new_source])

            seen[visiting] = time

        # go through nodes, adding to heap queue if not seen and popping the smallest
        # increase res by the amount it takes to reach, go through all 1s, 2s etc

        return max(seen.values()) if len(seen) == n else -1


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

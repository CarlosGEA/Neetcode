"""
Difficulty : Medium
Date created : 21-11-2024
"""

import heapq
from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        # cycle = 0

        # maxHeap = [-c for c in Counter(tasks).values()]
        # heapq.heapify(maxHeap)
        # queue = []
        # heapq.heapify(queue)

        # while maxHeap or queue:
        #     cycle += 1

        #     if maxHeap:
        #         val = heapq.heappop(maxHeap)
        #         val += 1

        #         if val:
        #             heapq.heappush(queue, (cycle + n, val))

        #     if queue and queue[0][0] == cycle:
        #         heapq.heappush(maxHeap, heapq.heappop(queue)[1])

        task_count = list(Counter(tasks).values())
        maxtask = max(task_count)

        nmax = task_count.count(maxtask)

        return max(len(tasks), (maxtask - 1) * (n + 1) + nmax)


def main():

    solution = Solution()

    tasks = ["X", "X", "Y", "Y"]
    n = 2
    print(f"The min cycle for all tasks is {solution.leastInterval(tasks, n)}")

    tasks = ["A", "A", "A", "B", "C"]
    n = 3
    print(f"The min cycle for all tasks is {solution.leastInterval(tasks, n)}")

    return None


if __name__ == "__main__":
    main()

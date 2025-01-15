"""
Difficulty : Medium
Date created : 15-01-2025
"""

from collections import deque


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        stops = 0
        mincost = float("inf")
        flightsDict = {i: [] for i in range(n)}

        for s, d, c in flights:
            flightsDict[s].append([d, c])

        queue = deque([[src, 0]])
        stops = 0
        while stops < k + 2:
            for _ in range(len(queue)):
                airport, cur_cost = queue.popleft()

                if airport == dst:
                    mincost = min(mincost, cur_cost)

                for dest, cost in flightsDict[airport]:
                    queue.append([dest, cur_cost + cost])

            stops += 1

        return mincost if mincost != float("inf") else -1


def main():
    solution = Solution()

    n = 4
    flights = [[0, 1, 200], [1, 2, 100], [1, 3, 300], [2, 3, 100]]
    src = 0
    dst = 3
    k = 1
    print(
        f"The cheapest flights to get from {src} to {dst} in max {k} stops is {solution.findCheapestPrice(n, flights, src, dst, k)}"
    )

    n = 3
    flights = [[1, 0, 100], [1, 2, 200], [0, 2, 100]]
    src = 1
    dst = 2
    k = 1
    print(
        f"The cheapest flights to get from {src} to {dst} in max {k} stops is {solution.findCheapestPrice(n, flights, src, dst, k)}"
    )

    return None


if __name__ == "__main__":
    main()

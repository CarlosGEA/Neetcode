"""
Difficulty : Medium
Date created : 31-01-2025
"""


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        # method

        # prims algorithm
        adj = {i: [] for i in range(n)}
        for s, d, c in flights:
            adj[s].append((d, c))

        res = [float("inf")] * n
        res[src] = 0

        for _ in range(k + 1):
            dummy = res.copy()
            for i, cost in enumerate(res):
                if cost == float("inf"):
                    continue

                for dest, new_cost in adj[i]:
                    dummy[dest] = min(dummy[dest], cost + new_cost)

            res = dummy
        return res[dst] if res[dst] != float("inf") else -1


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

    n = 8
    flights = [
        [3, 4, 7],
        [6, 2, 2],
        [0, 2, 7],
        [0, 1, 2],
        [1, 7, 8],
        [4, 5, 2],
        [0, 3, 2],
        [7, 0, 6],
        [3, 2, 7],
        [1, 3, 10],
        [1, 5, 1],
        [4, 1, 6],
        [4, 7, 5],
        [5, 7, 10],
    ]
    src = 4
    dst = 3
    k = 7
    print(
        f"The cheapest flights to get from {src} to {dst} in max {k} stops is {solution.findCheapestPrice(n, flights, src, dst, k)}"
    )

    return None


if __name__ == "__main__":
    main()

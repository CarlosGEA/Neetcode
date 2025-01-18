"""
Difficulty : Medium
Date created : 18-01-2025
New attempt : ??-01-2025
"""

from collections import deque


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        return


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

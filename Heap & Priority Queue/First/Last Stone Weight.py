"""
Difficulty : Easy
Date created : 15-11-2024
"""

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        maxheap = []
        heapq.heapify(maxheap)

        for i in stones:
            heapq.heappush(maxheap, -i)

        while maxheap:
            if len(maxheap) == 1:
                return -maxheap[0]

            first = heapq.heappop(maxheap)
            second = heapq.heappop(maxheap)

            if first == second:
                continue

            heapq.heappush(maxheap, -abs(first - second))

        return 0


def main():
    solution = Solution()

    stones = [2, 3, 6, 2, 4]
    print(f"The weight of the last remeaning stone is {solution.lastStoneWeight(stones)}")

    stones = [1, 2]
    print(f"The weight of the last remeaning stone is {solution.lastStoneWeight(stones)}")

    return None


if __name__ == "__main__":
    main()

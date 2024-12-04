"""
Difficulty : Easy
Date created : 04-12-2024
"""

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))

        stones.append(0)
        return -stones[0]


def main():
    solution = Solution()

    stones = [2, 3, 6, 2, 4]
    print(f"The weight of the last remeaning stone is {solution.lastStoneWeight(stones)}")

    stones = [1, 2]
    print(f"The weight of the last remeaning stone is {solution.lastStoneWeight(stones)}")

    return None


if __name__ == "__main__":
    main()

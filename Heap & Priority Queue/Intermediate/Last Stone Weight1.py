"""
Difficulty : Easy
Date created : 18-11-2024
"""

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            if s1 != s2:
                heapq.heappush(stones, s1 - s2)

        heapq.heappush(stones, 0)
        return -stones[0]


def main():
    solution = Solution()

    stones = [2, 3, 6, 2, 4]
    print(f"The remaining stone weight is {solution.lastStoneWeight(stones)}")

    stones = [1, 2]
    print(f"The remaining stone weight is {solution.lastStoneWeight(stones)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Easy
Date created : 18-01-2025
"""


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


def main():

    solution = Solution()

    cost = [1, 2, 3]
    print(f"The minimum cost to walk up the stairs is {solution.minCostClimbingStairs(cost)}")

    cost = [1, 2, 1, 2, 1, 1, 1]
    print(f"The minimum cost to walk up the stairs is {solution.minCostClimbingStairs(cost)}")

    return None


if __name__ == "__main__":
    main()

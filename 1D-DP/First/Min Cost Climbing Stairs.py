"""
Difficulty : Easy
Date created : 29-11-2024
"""


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)

        runcost = [None] * len(cost)
        runcost[0] = cost[0]
        runcost[1] = cost[1]

        for i in range(2, len(runcost)):
            runcost[i] = cost[i] + min(runcost[i - 1], runcost[i - 2])

        return runcost[-1]


def main():

    solution = Solution()

    cost = [1, 2, 3]
    print(f"The minimum cost to walk up the stairs is {solution.minCostClimbingStairs(cost)}")

    cost = [1, 2, 1, 2, 1, 1, 1]
    print(f"The minimum cost to walk up the stairs is {solution.minCostClimbingStairs(cost)}")

    return None


if __name__ == "__main__":
    main()

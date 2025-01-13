"""
Difficulty : Medium
Date created : 13-01-2025
"""


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        cur = tot = 0
        for i in range(len(cost)):
            tot += gas[i] - cost[i]
            if tot < 0:
                tot = 0
                cur = i + 1

        return cur


def main():

    solution = Solution()

    gas = [1, 2, 3, 4]
    cost = [2, 2, 4, 1]
    print(
        f"The starting index where a car can make a circuit is {solution.canCompleteCircuit(gas, cost)}"
    )

    gas = [1, 2, 3]
    cost = [2, 3, 2]
    print(
        f"The starting index where a car can make a circuit is {solution.canCompleteCircuit(gas, cost)}"
    )

    return None


if __name__ == "__main__":
    main()

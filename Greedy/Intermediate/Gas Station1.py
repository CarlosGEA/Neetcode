"""
Difficulty : Medium
Date created : 10-01-2025
"""


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # make O(n) - two pointers then greedy
        tot = 0
        pot = 0
        for i in range(len(gas)):
            cur = gas[i] - cost[i]
            tot += cur
            if tot < 0 and cur < 0:
                pot = i + 1

        return pot if tot >= 0 else -1


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

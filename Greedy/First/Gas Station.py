"""
Difficulty : Medium
Date created : 07-01-2025
"""


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        n = len(gas)
        for start in range(n):
            tot_gas = 0
            for i in range(start, start + n):
                idx = i % n
                tot_gas = tot_gas + gas[idx] - cost[idx]
                if tot_gas < 0:
                    break

            else:
                return start

        return -1


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

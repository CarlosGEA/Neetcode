"""
Difficulty : Medium
Date created : 13-12-2024
"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        res = [float("inf")] * (amount + 1)
        res[0] = 0

        for i in range(len(res)):
            for c in coins:
                if c + i <= amount:
                    res[c + i] = min(res[c + i], 1 + res[i])

        return res[amount] if res[amount] != float("inf") else -1


def main():

    solution = Solution()

    coins = [1, 5, 10]
    amount = 12
    # coins = [2147483647]
    # amount = 2
    print(
        f"The minimum number of coins needed to make {amount} is {solution.coinChange(coins, amount)}"
    )

    coins = [2]
    amount = 3
    print(
        f"The minimum number of coins needed to make {amount} is {solution.coinChange(coins, amount)}"
    )

    coins = [1]
    amount = 0
    print(
        f"The minimum number of coins needed to make {amount} is {solution.coinChange(coins, amount)}"
    )

    coins = [25, 10, 5, 2, 1, 50, 100, 20, 40, 60]
    amount = 200
    print(
        f"The minimum number of coins needed to make {amount} is {solution.coinChange(coins, amount)}"
    )

    return None


if __name__ == "__main__":
    main()

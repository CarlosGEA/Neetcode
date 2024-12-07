"""
Difficulty : Medium
Date created : 06-12-2024
New attempt : 
"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins.sort()
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[0] = [0] + [float("inf")] * amount
        for i in range(1, n + 1):
            for j in range(coins[i - 1]):
                dp[i][j] = dp[i - 1][j]
            for j in range(coins[i - 1], amount + 1):
                dp[i][j] = min(dp[i][j - coins[i - 1]] + 1, dp[i - 1][j])

        res = min([ans[-1] for ans in dp])
        return res if res != float("inf") else -1


def main():

    solution = Solution()

    # coins = [1, 5, 10]
    # amount = 12
    coins = [2147483647]
    amount = 2

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

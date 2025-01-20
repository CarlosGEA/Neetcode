"""
Difficulty : Medium
Date created : 20-01-2025
"""


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # good coins then amount
        res = [0] * (amount + 1)
        res[0] = 1
        for coin in coins:
            for i in range(0, len(res)):
                if i + coin <= amount:
                    res[i + coin] += res[i]

        return res[amount]


def main():

    solution = Solution()

    amount = 4
    coins = [1, 2, 3]
    print(
        f"The number of ways to make {amount} using unlimited amount of {coins} is {solution.change(amount, coins)}"
    )

    amount = 7
    coins = [2, 4]
    print(
        f"The number of ways to make {amount} using unlimited amount of {coins} is {solution.change(amount, coins)}"
    )

    return None


if __name__ == "__main__":
    main()

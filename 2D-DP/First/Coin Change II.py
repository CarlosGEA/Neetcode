"""
Difficulty : Medium
Date created : 17-01-2025
"""


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        res = [0] * (amount + 0)
        res.append(1)

        for c in coins:
            for i in range(len(res) - 1, 0, -1):
                if i - c >= 0:
                    res[i - c] += res[i]

        return res[0]


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

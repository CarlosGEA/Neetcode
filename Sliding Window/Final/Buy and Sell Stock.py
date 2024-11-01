"""
Difficulty : Easy
Date created : 31-10-2024
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        l = 0
        maxp = 0
        for r, p in enumerate(prices):
            maxp = max(maxp, p - prices[l])
            if p < prices[l]:
                l = r

        return maxp


def main():

    solution = Solution()

    prices = [10, 1, 5, 6, 7, 1]
    print(f"The max profit that can be made is {solution.maxProfit(prices)}")

    prices = [10, 8, 7, 5, 2]
    print(f"The max profit that can be made is {solution.maxProfit(prices)}")

    return None


if __name__ == "__main__":
    main()

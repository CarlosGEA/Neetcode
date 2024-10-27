"""
Difficulty : Easy
Date created : 26-10-2024
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # sliding window/ two pointer
        l = 0
        maxP = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r

            maxP = max(maxP, prices[r] - prices[l])

        return maxP


def main():

    solution = Solution()

    prices = [10, 1, 5, 6, 7, 1]
    print(f"The max profit that can be made is {solution.maxProfit(prices)}")

    prices = [10, 8, 7, 5, 2]
    print(f"The max profit that can be made is {solution.maxProfit(prices)}")

    return None


if __name__ == "__main__":
    main()

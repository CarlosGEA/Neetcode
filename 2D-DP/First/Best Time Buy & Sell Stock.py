"""
Difficulty : Medium
Date created : 16-01-2025
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        res = [0] * (len(prices) + 2)

        for i in range(len(prices) - 2, -1, -1):
            # curmax = 0
            for j in range(i + 1, len(prices)):
                # curmax = max(curmax, res[j + 1])
                res[i] = max(res[i], prices[j] - prices[i] + res[j + 2])

        return max(res)


def main():

    solution = Solution()

    prices = [1, 3, 4, 0, 4]
    print(f"The most profit from buying and selling coins is {solution.maxProfit(prices)}")

    prices = [1]
    print(f"The most profit from buying and selling coins is {solution.maxProfit(prices)}")

    return None


if __name__ == "__main__":
    main()

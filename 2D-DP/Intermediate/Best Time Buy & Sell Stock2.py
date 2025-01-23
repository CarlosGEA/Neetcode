"""
Difficulty : Medium
Date created : 25-01-2025
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        memo = {}

        def dfs(i, buy):
            if i >= len(prices):
                return 0

            if (i, buy) in memo:
                return memo[(i,buy)]

            cooldown = dfs(i + 1, buy)
            if buy:
                res = max(dfs(i + 1, not buy) - prices[i], cooldown)

            else:
                res = max(dfs(i + 2, not buy) + prices[i], cooldown)

            memo[(i, buy)] = res
            return res

        return dfs(0, True)

def main():

    solution = Solution()

    prices = [1, 3, 4, 0, 4]
    print(f"The most profit from buying and selling coins is {solution.maxProfit(prices)}")

    prices = [1]
    print(f"The most profit from buying and selling coins is {solution.maxProfit(prices)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Hard
Date created : 01-02-2025
"""


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}

        def dfs(l, r):

            if l > r:
                return 0

            if (l, r) in cache:
                return cache[(l, r)]

            res = 0
            for i in range(l, r + 1):
                coins = (nums[l - 1] * nums[i] * nums[r + 1]) + dfs(l, i - 1) + dfs(i + 1, r)
                res = max(res, coins)

            cache[(l, r)] = res
            return res

        return dfs(1, len(nums) - 2)


def main():

    solution = Solution()

    nums = [4, 2, 3, 7]
    print(f"The maximum amount of coins gained by popping balloons is {solution.maxCoins(nums)}")

    nums = [3, 1, 5, 8]
    print(f"The maximum amount of coins gained by popping balloons is {solution.maxCoins(nums)}")

    return None


if __name__ == "__main__":
    main()

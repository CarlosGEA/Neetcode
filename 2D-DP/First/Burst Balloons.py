"""
Difficulty : Hard
Date created : 22-01-2025
New attempt : 26-01-2025
New attempt : 29-01-2025
"""

# If you burst the ith balloon, you will receive nums[i - 1] * nums[i] * nums[i + 1] coins.
#  If i - 1 or i + 1 goes out of bounds of the array, then assume the out of bounds value is 1.


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # left and right from where we are popping last, calculate current coins

        nums = [1] + nums + [1]

        memo = {}

        def dfs(l, r):

            if l > r:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            res = 0
            for i in range(l, r + 1):
                res = max(
                    res,
                    (nums[l - 1] * nums[i] * nums[r + 1])
                    + dfs(l, i - 1)
                    + dfs(i + 1, r),
                )

            memo[(l, r)] = res
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

"""
Difficulty : Medium
Date created : 18-01-2025
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        res = float("-inf")

        def dfs(cur, i):
            nonlocal res
            if i == len(nums):
                return
            res = max(res, cur * nums[i], nums[i])
            dfs(cur * nums[i], i + 1)
            dfs(nums[i], i + 1)

            return

        dfs(1, 0)
        return res


def main():

    solution = Solution()

    nums = [1, 2, -3, 4]
    print(f"The maximum product of a subarray is {solution.maxProduct(nums)}")

    nums = [-2, -1]
    print(f"The maximum product of a subarray is {solution.maxProduct(nums)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 18-01-2025
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curMin = 1
        curMax = 1
        res = float("-inf")

        for num in nums:
            tmp = curMin
            curMin = min(num, curMax * num, curMin * num)
            curMax = max(num, curMax * num, tmp * num)
            res = max(res, curMax)

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

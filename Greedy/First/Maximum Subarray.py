"""
Difficulty : Medium
Date created : 19-12-2024
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        res = float("-inf")

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                res = max(res, sum(nums[i : j + 1]))

        return res


def main():

    solution = Solution()

    nums = [2, -3, 4, -2, 2, 1, -1, 4]
    print(f"The maximum sum of a subarray in nums is {solution.maxSubArray(nums)}")

    nums = [-1]
    print(f"The maximum sum of a subarray in nums is {solution.maxSubArray(nums)}")

    return None


if __name__ == "__main__":
    main()

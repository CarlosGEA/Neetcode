"""
Difficulty : Medium
Date created : 09-01-2025
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0]
        cur = 0

        for n in nums:
            cur += n
            res = max(cur, res)

            if cur < 0:
                cur = 0

        return res


def main():

    solution = Solution()

    nums = [2, -3, 4, -2, 2, 1, -1, 4]
    print(f"The maximum sum in a subarray is {solution.maxSubArray(nums)}")

    nums = [-1]
    print(f"The maximum sum in a subarray is {solution.maxSubArray(nums)}")

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"The maximum sum in a subarray is {solution.maxSubArray(nums)}")

    return None


if __name__ == "__main__":
    main()

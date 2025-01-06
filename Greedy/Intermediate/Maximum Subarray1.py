"""
Difficulty : 
Date created : 06-01-2025
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # not brute force method, use kadane's alg
        cur = float("-inf")
        res = cur
        for i in range(len(nums)):
            if cur < 0 and nums[i] > cur:
                cur = nums[i]
            else:
                cur += nums[i]

            res = max(res, cur)
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

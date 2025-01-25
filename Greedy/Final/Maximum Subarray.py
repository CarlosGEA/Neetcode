"""
Difficulty : Medium
Date created : 24-01-2025
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = float("-inf")
        cur = 0
        for num in nums:
            if cur < 0:
                cur = 0
            cur += num
            res = max(res, cur)

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

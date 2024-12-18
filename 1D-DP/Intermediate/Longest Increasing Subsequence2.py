"""
Difficulty : Medium
Date created : 18-12-2024
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # double loop
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    dp[j] = max(dp[i] + 1, dp[j])
        return max(dp)


def main():

    solution = Solution()

    nums = [9, 1, 4, 2, 3, 3, 7]
    print(f"The length of the longest increasing subsequence is {solution.lengthOfLIS(nums)}")

    nums = [0, 3, 1, 3, 2, 3]
    print(f"The length of the longest increasing subsequence is {solution.lengthOfLIS(nums)}")

    return None


if __name__ == "__main__":
    main()

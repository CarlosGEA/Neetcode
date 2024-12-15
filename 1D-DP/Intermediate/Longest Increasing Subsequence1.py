"""
Difficulty : Medium
Date created : 15-12-2024
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        res = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res[j] = max(res[j], res[i] + 1)
        return max(res)


def main():

    solution = Solution()

    nums = [9, 1, 4, 2, 3, 3, 7]
    print(f"The length of the longest increasing subsequence is {solution.lengthOfLIS(nums)}")

    nums = [0, 3, 1, 3, 2, 3]
    print(f"The length of the longest increasing subsequence is {solution.lengthOfLIS(nums)}")

    return None


if __name__ == "__main__":
    main()

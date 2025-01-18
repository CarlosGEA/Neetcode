"""
Difficulty : Medium
Date created : 18-01-2025
Next attempt : ??-01-2025
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        res = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                res[i] += res[i + 1]
            else:
                res[i] = res[i + 1]

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

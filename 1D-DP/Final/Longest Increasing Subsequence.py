"""
Difficulty : Medium
Date created : 18-01-2025
Next attempt : 21-01-2025
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # doulbe for

        res = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
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

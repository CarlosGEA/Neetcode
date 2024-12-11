"""
Difficulty : Medium
Date created : 10-12-2024
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:

        res = [1] * len(nums)

        for i in range(len(res), -1, -1):
            for j in range(len(res) - 1, i, -1):
                # print(nums[i], nums[j])
                if nums[j] > nums[i]:
                    res[i] = max(res[i], 1 + res[j]) 

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

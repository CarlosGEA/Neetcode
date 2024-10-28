"""
Difficulty : Medium
Date created : -10-2024
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:


        return


def main():

    solution = Solution()

    nums = [-1, 0, 1, 2, -1, -4]
    print(f"The possible triplets that sum to 0 are {solution.threeSum(nums)}")

    nums = [0, 1, 1]
    print(f"The possible triplets that sum to 0 are {solution.threeSum(nums)}")

    nums = [0, 0, 0, 0]
    print(f"The possible triplets that sum to 0 are {solution.threeSum(nums)}")

    return None


if __name__ == "__main__":
    main()

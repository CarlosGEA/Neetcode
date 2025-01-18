"""
Difficulty : Medium
Date created : 18-01-2025
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        nums.append(0)
        for i in range(len(nums) - 4, -1, -1):
            nums[i] += max(nums[i + 2], nums[i + 3])
        nums.append(0)
        return max(nums[0], nums[1])


def main():

    solution = Solution()

    nums = [3, 4, 3]
    print(f"The max amount of money to rob is {solution.rob(nums)}")

    nums = [2, 9, 8, 3, 6]
    print(f"The max amount of money to rob is {solution.rob(nums)}")

    nums = [1, 9, 2, 2, 8]
    print(f"The max amount of money to rob is {solution.rob(nums)}")

    nums = [1, 2, 3, 1]
    print(f"The max amount of money to rob is {solution.rob(nums)}")

    return None


if __name__ == "__main__":
    main()

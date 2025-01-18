"""
Difficulty : Medium
Date created : 18-01-2025
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        nums.append(0)
        for i in range(len(nums) - 4, -1, -1):
            nums[i] += max(nums[i + 2], nums[i + 3])

        return max(nums[0], nums[1])


def main():

    solution = Solution()

    nums = [1, 1, 3, 3]
    print(f"The max amount of money to rob is {solution.rob(nums)}")

    # nums = [2, 9, 8, 3, 6]
    nums = [1, 9, 2, 2, 8]
    print(f"The max amount of money to rob is {solution.rob(nums)}")

    return None


if __name__ == "__main__":
    main()

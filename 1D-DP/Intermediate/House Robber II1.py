"""
Difficulty : Medium
Date created : 05-12-2024
"""


class Solution:
    def rob(self, nums: list[int]) -> int:

        max1 = self.rob_norm(nums[1:])
        max2 = self.rob_norm(nums[:-1])

        return max(nums[0], max1, max2)

    def rob_norm(self, nums):

        nums.append(0)
        for n in range(len(nums) - 3, -1, -1):
            nums[n] = max(nums[n + 1], nums[n] + nums[n + 2])
        nums.append(0)

        return max(nums[0], nums[1])


def main():

    solution = Solution()

    nums = [3, 4, 3]
    print(f"The max that can be robbed is {solution.rob(nums)}")

    nums = [2, 9, 8, 3, 6]
    print(f"The max that can be robbed is {solution.rob(nums)}")

    nums = [1, 2, 3, 1]
    print(f"The max that can be robbed is {solution.rob(nums)}")

    return None


if __name__ == "__main__":
    main()

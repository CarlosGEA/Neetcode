"""
Difficulty : Medium
Date created : 06-12-2024
"""


class Solution:
    def rob(self, nums: list[int]) -> int:

        # rob1 = 0
        # rob2 = 0

        # for n in nums:
        #     temp = max(rob2, rob1 + n)
        #     rob1 = rob2
        #     rob2 = temp

        # return rob2

        for i in range(len(nums) - 3, -1, -1):
            nums[i] = max(nums[i+1], nums[i] + nums[i+2])
        nums.append(0)
        return max(nums[0], nums[1])


def main():

    solution = Solution()

    nums = [1, 1, 3, 3]
    print(f"The max amount that can be robbed is {solution.rob(nums)}")

    nums = [2, 9, 8, 3, 6]
    print(f"The max amount that can be robbed is {solution.rob(nums)}")

    return None


if __name__ == "__main__":
    main()

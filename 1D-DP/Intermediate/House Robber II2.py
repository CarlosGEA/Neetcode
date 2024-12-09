"""
Difficulty : Medium
Date created : 09-12-2024
"""


class Solution:
    def rob(self, nums: list[int]) -> int:

        return max(nums[0], self.rob2(nums[1:]), self.rob2(nums[:-1]))

    def rob2(self, nums):
        h1 = 0
        h2 = 0

        for n in nums:
            temp = max(h2, h1 + n)
            h1 = h2
            h2 = temp

        return h2


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

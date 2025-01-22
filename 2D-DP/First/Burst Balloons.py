"""
Difficulty : Hard
Date created : 22-01-2025
New attempt : 25-01-2025
"""

# If you burst the ith balloon, you will receive nums[i - 1] * nums[i] * nums[i + 1] coins.
#  If i - 1 or i + 1 goes out of bounds of the array, then assume the out of bounds value is 1.


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        return


def main():

    solution = Solution()

    nums = [4, 2, 3, 7]
    print(f"The maximum amount of coins gained by popping balloons is {solution.maxCoins(nums)}")

    nums = [3, 1, 5, 8]
    print(f"The maximum amount of coins gained by popping balloons is {solution.maxCoins(nums)}")

    return None


if __name__ == "__main__":
    main()

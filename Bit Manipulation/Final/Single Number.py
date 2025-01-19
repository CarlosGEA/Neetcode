"""
Difficulty : Easy
Date created : 19-01-2025
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        n = nums[0]
        for num in nums[1:]:
            n ^= num

        return n


def main():

    solution = Solution()

    nums = [3, 2, 3]
    print(f"The non repeat number in the array is {solution.singleNumber(nums)}")

    nums = [7, 6, 6, 7, 8]
    print(f"The non repeat number in the array is {solution.singleNumber(nums)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Easy
Date created : 20-12-2024
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        x = nums[0]

        for n in nums[1:]:
            x ^= n
        return x


def main():

    solution = Solution()

    nums = [3, 2, 3]
    print(f"The non repeat number in the array is {solution.singleNumber(nums)}")

    nums = [7, 6, 6, 7, 8]
    print(f"The non repeat number in the array is {solution.singleNumber(nums)}")

    return None


if __name__ == "__main__":
    main()

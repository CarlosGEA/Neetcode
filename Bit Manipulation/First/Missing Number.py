"""
Difficulty : Easy
Date created : 18-12-2024
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return (n * (n + 1)) // 2 - sum(nums)


def main():

    solution = Solution()

    nums = [1, 2, 3]
    print(f"The missing number in the range 0-{len(nums)} is {solution.missingNumber(nums)}")

    nums = [0, 2]
    print(f"The missing number in the range 0-{len(nums)} is {solution.missingNumber(nums)}")

    return None


if __name__ == "__main__":
    main()

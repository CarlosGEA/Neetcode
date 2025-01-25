"""
Difficulty : Medium
Date created : 24-01-2025
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        i = 0
        for j, num in enumerate(nums):
            if j <= i:
                i = max(i, j + num)

        return i >= len(nums) - 1


def main():

    solution = Solution()

    nums = [1, 2, 0, 1, 0]
    print(f"Can the last tile be reached? : {solution.canJump(nums)}")

    nums = [1, 2, 1, 0, 1]
    print(f"Can the last tile be reached? : {solution.canJump(nums)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 20-12-2024
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        res = [False] * len(nums)
        res[0] = True

        for i in range(len(nums)):
            for j in range(i + 1, i + nums[i] + 1):
                if j < len(nums):
                    res[j] = res[i]

        return res[-1]


def main():

    solution = Solution()

    nums = [1, 2, 0, 1, 0]
    print(f"Can the last tile be reached? : {solution.canJump(nums)}")

    nums = [1, 2, 1, 0, 1]
    print(f"Can the last tile be reached? : {solution.canJump(nums)}")

    return None


if __name__ == "__main__":
    main()

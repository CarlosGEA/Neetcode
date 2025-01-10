"""
Difficulty : Medium
Date created : 10-01-2025
"""


class Solution:
    def jump(self, nums: list[int]) -> int:
        furthest = 0
        res = 0
        for i, n in enumerate(nums):

            if furthest >= len(nums) - 1:
                return res

            if i + nums[i] > furthest:
                furthest = i + nums[i]
                res += 1

        return res


def main():

    solution = Solution()

    nums = [2, 4, 1, 1, 1, 1]
    print(f"The minimum number of jumps needed to reach the end is {solution.jump(nums)}")

    nums = [2, 1, 2, 1, 0]
    print(f"The minimum number of jumps needed to reach the end is {solution.jump(nums)}")

    return None


if __name__ == "__main__":
    main()

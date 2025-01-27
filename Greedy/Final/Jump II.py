"""
Difficulty : Medium
Date created : 24-01-2025
New attempt : 27-01-2025
"""


class Solution:
    def jump(self, nums: list[int]) -> int:
        # left and right#
        res = 0
        l = r = 0
        while r < len(nums) - 1:

            for i in range(l, r + 1):
                if nums[i] + i > r:
                    l = r + 1
                    r = nums[i] + i

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

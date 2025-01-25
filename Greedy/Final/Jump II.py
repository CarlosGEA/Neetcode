"""
Difficulty : Medium
Date created : 24-01-2025
New attempt : 27-01-2025
"""


class Solution:
    def jump(self, nums: list[int]) -> int:
        # good - maybe can optimize using l, r ??
        res = 0
        cur = 0
        while cur < len(nums) - 1:
            for j in range(cur, -1, -1):
                if j + nums[j] > cur:
                    cur = j + nums[j]
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

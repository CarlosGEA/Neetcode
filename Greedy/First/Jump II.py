"""
Difficulty : Medium
Date created : 07-01-2025
"""


class Solution:
    def jump(self, nums: list[int]) -> int:

        goal = len(nums) - 1
        res = 0

        while goal:
            for j in range(0, goal):
                if j + nums[j] >= goal:
                    res += 1
                    goal = j
                    break

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

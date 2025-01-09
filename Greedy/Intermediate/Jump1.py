"""
Difficulty : 
Date created : 06-01-2025
New attempt : 09-01-2025
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # can improve complexity to O(n)

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):

            if i + nums[i] >= goal:
                goal = i

        return goal == 0


def main():

    solution = Solution()

    nums = [1, 2, 0, 1, 0]
    print(f"It is possible to reach the last position : {solution.canJump(nums)}")

    nums = [1, 2, 1, 0, 1]
    print(f"It is possible to reach the last position : {solution.canJump(nums)}")

    return None


if __name__ == "__main__":
    main()

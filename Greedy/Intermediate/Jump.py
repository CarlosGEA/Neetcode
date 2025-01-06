"""
Difficulty : 
Date created : 06-01-2025
New attempt : -01-2025
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # can improve complexity to O(n)

        return

def main():

    solution = Solution()

    nums = [1, 2, 0, 1, 0]
    print(f"It is possible to reach the last position : {solution.canJump(nums)}")

    nums = [1, 2, 1, 0, 1]
    print(f"It is possible to reach the last position : {solution.canJump(nums)}")

    return None


if __name__ == "__main__":
    main()

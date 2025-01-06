"""
Difficulty : Easy
Date created : 06-01-2025
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        res = n 
        for i in range(n):
            res ^= nums[i]
            res ^= i

        return res


def main():

    solution = Solution()

    nums = [1, 2, 3]
    print(f"The missing number in the range 0-{len(nums)} is {solution.missingNumber(nums)}")

    nums = [0, 2]
    print(f"The missing number in the range 0-{len(nums)} is {solution.missingNumber(nums)}")

    return None


if __name__ == "__main__":
    main()

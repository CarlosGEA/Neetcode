"""
Difficulty : Medium
Date created : 15-10-2024
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Use only preffix and suffix
        
        return


def main():

    solution = Solution()

    nums = [1, 2, 4, 6]
    print(f"The product of numbers in the array except self is {solution.productExceptSelf(nums)}")

    nums = [-1, 0, 1, 2, 3]
    print(f"The product of numbers in the array except self is {solution.productExceptSelf(nums)}")

    return None


if __name__ == "__main__":
    main()

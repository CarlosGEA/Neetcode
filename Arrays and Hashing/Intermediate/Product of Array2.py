"""
Difficulty : Medium
Date created : 17-10-2024
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = nums[0]
        res = [1] * n
        for i in range(1, n):
            res[i] *= left # =
            left *= nums[i]      
        
        right = nums[-1]
        for i in range(n - 2, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res


def main():

    solution = Solution()

    nums = [1, 2, 4, 6]
    print(f"The product of numbers in the array except self is {solution.productExceptSelf(nums)}")

    nums = [-1, 0, 1, 2, 3]
    print(f"The product of numbers in the array except self is {solution.productExceptSelf(nums)}")

    return None


if __name__ == "__main__":
    main()

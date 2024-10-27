"""
Difficulty : Medium
Date created : 26-10-2024
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        left = 1
        for i in range(n):
            res[i] *= left
            left *= nums[i]

        right = 1

        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res


def main():

    solution = Solution()

    nums = [1, 2, 4, 6]
    print(
        f"The output array for product sums disincluding self is {solution.productExceptSelf(nums)}"
    )

    nums = [-1, 0, 1, 2, 3]
    print(
        f"The output array for product sums disincluding self is {solution.productExceptSelf(nums)}"
    )

    return None


if __name__ == "__main__":
    main()

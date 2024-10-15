"""
Difficulty : Medium
Date created : 15-10-2024
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zeros = []
        total_prod = 1
        for idx, n in enumerate(nums):
            if n == 0:
                zeros.append(idx)
                continue
            total_prod *= n

        if len(zeros) > 1:
            return [0] * len(nums)

        elif len(zeros) == 1:
            ans = [0] * len(nums)
            ans[zeros[0]] = total_prod
            return ans

        right = [1] * len(nums)
        for i in range(1, len(nums)):
            right[i] = right[i - 1] * nums[i - 1]

        left = [1] * len(nums)
        for i in range(len(nums) - 1, 0, -1):
            left[i - 1] = left[i] * nums[i]


        res = [1] * len(nums)
        for i in range(len(res)):
            res[i] = right[i] * left[i]

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

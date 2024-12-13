"""
Difficulty : Medium
Date created : 13-12-2024
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # store, current max and min and save the result at each loop
        res = float("-inf")
        curmin = 1
        curmax = 1

        for n in nums:
            tmp = curmax
            curmax = max(n, n * curmin, n * curmax)
            curmin = min(n, n * curmin, n * tmp)

            res = max(res, curmax)

        return res


def main():

    solution = Solution()

    nums = [1, 2, -3, 4]
    print(f"The maximum product of a subarray is {solution.maxProduct(nums)}")

    # nums = [-2, -1]
    nums = [-2, 0, -1]
    print(f"The maximum product of a subarray is {solution.maxProduct(nums)}")

    nums = [-4, -3, -2]
    print(f"The maximum product of a subarray is {solution.maxProduct(nums)}")

    return None


if __name__ == "__main__":
    main()

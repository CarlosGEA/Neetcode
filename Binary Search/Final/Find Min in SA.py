"""
Difficulty : Medium
Date created : 03-11-2024
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = float("inf")

        while l <= r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

            res = min(res, nums[m])

        return res


def main():

    solution = Solution()

    nums = [3, 4, 5, 6, 1, 2]
    print(f"The minimum in {nums} is {solution.findMin(nums)}")

    nums = [4, 5, 0, 1, 2, 3]
    print(f"The minimum in {nums} is {solution.findMin(nums)}")

    nums = [4, 5, 6, 7]
    print(f"The minimum in {nums} is {solution.findMin(nums)}")

    return None


if __name__ == "__main__":
    main()

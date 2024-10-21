"""
Difficulty : Medium
Date created : 20-10-2024
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:

        l = 0
        r = len(nums) - 1
        min_num = float("inf")

        while l < r:
            if nums[l] > nums[r]:
                l += 1
                min_num = min(min_num, nums[r])
            else:
                r -= 1
                min_num = min(min_num, nums[l])

        return min_num


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

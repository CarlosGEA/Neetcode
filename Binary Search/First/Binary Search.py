"""
Difficulty : Easy
Date created : 18-10-2024
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = ((l + r) // 2) 
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1


def main():

    solution = Solution()

    nums = [-1, 0, 2, 4, 6, 8]
    target = 4
    print(f"The index of the solution is {solution.search(nums, target)}")

    nums = [-1, 0, 2, 4, 6, 8]
    target = 3
    print(f"The index of the solution is {solution.search(nums, target)}")

    nums = [5]
    target = 5
    print(f"The index of the solution is {solution.search(nums, target)}")


    return None


if __name__ == "__main__":
    main()

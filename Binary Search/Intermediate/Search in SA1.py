"""
Difficulty : Medium
Date created : 23-10-2024
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if target > nums[m]:
                if target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

            else:
                if target >= nums[l] or target < nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1


def main():

    solution = Solution()

    # nums = [3, 4, 5, 6, 1, 2]
    # target = 1
    # print(f"The target number {target} in this array has index {solution.search(nums, target)}")

    # nums = [3, 5, 6, 0, 1, 2]
    # target = 4
    # print(f"The target number {target} in this array has index {solution.search(nums, target)}")

    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 0
    # print(f"The target number {target} in this array has index {solution.search(nums, target)}")    
    
    nums = [5, 1, 2, 3, 4]
    target = 1
    print(f"The target number {target} in this array has index {solution.search(nums, target)}")

    return None


if __name__ == "__main__":
    main()

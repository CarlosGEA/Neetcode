"""
Difficulty : Medium
Date created : 03-11-2024
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            elif nums[m] > nums[r]:
                if nums[m] < target or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] > target or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1

        return -1


def main():

    solution = Solution()

    nums = [3, 4, 5, 6, 1, 2]
    target = 1
    print(f"The target number has been found at index {solution.search(nums, target)}")

    nums = [3, 5, 6, 0, 1, 2]
    target = 4
    print(f"The target number has been found at index {solution.search(nums, target)}")

    nums = [5, 1, 3]
    target = 5
    print(f"The target number has been found at index {solution.search(nums, target)}")

    return None


if __name__ == "__main__":
    main()

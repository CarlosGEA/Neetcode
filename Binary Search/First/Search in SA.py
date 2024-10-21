"""
Difficulty : Medium
Date created : 20-10-2024
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[l] <= target < nums[m]:
                r = m - 1

            elif nums[m] < target <= nums[r]:
                l = m + 1

            elif target < nums[m] <= nums[r]:
                r = m - 1

            elif nums[m] <= nums[r] < target:
                r = m - 1
            else:
                l = m + 1

        return -1


def main():

    solution = Solution()

    nums = [3, 4, 5, 6, 1, 2]
    target = 1
    print(
        f"The target number, {target} has {'not ' if solution.search(nums, target) == -1 else ''}been found"
    )

    nums = [3, 5, 6, 0, 1, 2]
    target = 4
    print(
        f"The target number, {target} has {'not ' if solution.search(nums, target) == -1 else ''}been found"
    )

    nums = [5, 1, 3]
    target = 5
    print(
        f"The target number, {target} has {'not ' if solution.search(nums, target) == -1 else ''}been found"
    )
    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Easy
Date created : 26-10-2024
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        need = {}

        for i, n in enumerate(nums):
            diff = target - n
            if n in need:
                return [need[n], i]

            need[diff] = i


def main():

    solution = Solution()

    nums = [3, 4, 5, 6]
    target = 7
    print(
        f"The two integer sum for target number {target} has indices: {solution.twoSum(nums, target)}"
    )

    nums = [4, 5, 6]
    target = 10
    print(
        f"The two integer sum for target number {target} has indices: {solution.twoSum(nums, target)}"
    )

    nums = [5, 5]
    target = 10
    print(
        f"The two integer sum for target number {target} has indices: {solution.twoSum(nums, target)}"
    )

    return None


if __name__ == "__main__":
    main()

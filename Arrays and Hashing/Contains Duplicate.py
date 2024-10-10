"""
Difficulty : Easy
Date created : 10-10-2024
"""


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


def main():

    solution = Solution()

    nums = [1, 2, 3, 3]
    print(f"The list {nums} has duplicates? : {solution.hasDuplicate(nums)}")

    nums = [1, 2, 3, 4]
    print(f"The list {nums} has duplicates? : {solution.hasDuplicate(nums)}")

    return None


if __name__ == "__main__":
    main()

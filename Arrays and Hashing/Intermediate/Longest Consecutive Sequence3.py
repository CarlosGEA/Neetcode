"""
Difficulty : Medium
Date created : 20-10-2024
"""
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        numSet = {}

        if not nums:
            return 0

        for n in nums:
            # if n - 1 not in numSet.keys() and n + 1 not in numSet.keys():
            #     numSet[n] = 1
            # else:
            numSet[n] = numSet.get(n - 1, 0) + numSet.get(n + 1, 0) + 1
            numSet[n - numSet.get(n - 1, 0)] = numSet[n]
            numSet[n + numSet.get(n + 1, 0)] = numSet[n]

        return max(numSet.values())


def main():

    solution = Solution()

    # nums = [2, 20, 4, 10, 3, 4, 5]
    nums = nums = [0, -1]
    print(f"The longest consecutive sequence is {solution.longestConsecutive(nums)} long")

    nums = [0, 3, 2, 5, 4, 6, 1, 1]
    print(f"The longest consecutive sequence is {solution.longestConsecutive(nums)} long")

    return None


if __name__ == "__main__":
    main()

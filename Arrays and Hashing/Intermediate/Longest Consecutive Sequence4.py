"""
Difficulty : Medium
Date created : 20-10-2024
"""

from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        mp = defaultdict(int)
        numSet = set(nums)
        res = 0

        for i in numSet:
            mp[i] = mp[i - 1] + mp[i + 1] + 1
            mp[i - mp[i - 1]] = mp[i]
            mp[i + mp[i + 1]] = mp[i]
            res = max(res, mp[i])

        return res


def main():

    solution = Solution()

    nums = [2, 20, 4, 10, 3, 4, 5]
    # nums = nums = [0, -1]
    print(f"The longest consecutive sequence is {solution.longestConsecutive(nums)} long")

    nums = [0, 3, 2, 5, 4, 6, 1, 1]
    print(f"The longest consecutive sequence is {solution.longestConsecutive(nums)} long")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 21-01-2025
"""

from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            new_dp = defaultdict(int)
            for val, count in dp.items():
                new_dp[val + num] += count
                new_dp[val - num] += count

            dp = new_dp

        return dp[target]


def main():

    solution = Solution()

    nums = [2, 2, 2]
    target = 2
    print(
        f"The total number of combinations to make {target} using {nums} is {solution.findTargetSumWays(nums, target)}"
    )

    return None


if __name__ == "__main__":
    main()

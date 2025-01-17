"""
Difficulty : Medium
Date created : 17-01-2025
"""


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        res = 0

        def dfs(cur, i):
            nonlocal res
            if i >= len(nums):
                if cur == target:
                    res += 1
                return

            dfs(cur + nums[i], i + 1)
            dfs(cur - nums[i], i + 1)

            return

        dfs(0, 0)
        return res


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

"""
Difficulty : Medium
Date created : 13-11-2024
"""


class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        nums.sort()

        def backtrack(i, cur, tot):

            if tot == target:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):
                if tot + nums[j] > target:
                    return

                cur.append(nums[j])
                backtrack(j, cur, tot + nums[j])
                cur.pop()

        backtrack(0, [], 0)
        return res


def main():

    solution = Solution()

    nums = [2, 5, 6, 9]
    target = 9
    print(f"The possible combinations to make {target} are {solution.combinationSum(nums, target)}")

    nums = [3, 4, 5]
    target = 16
    print(f"The possible combinations to make {target} are {solution.combinationSum(nums, target)}")

    nums = [3]
    target = 5
    print(f"The possible combinations to make {target} are {solution.combinationSum(nums, target)}")

    return None


if __name__ == "__main__":
    main()

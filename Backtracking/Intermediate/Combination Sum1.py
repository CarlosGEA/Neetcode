"""
Difficulty : Medium
Date created : 10-11-2024
"""


class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:

        res = []
        nums.sort()

        def backtrack(cur, i, val):

            if val == target:
                res.append(cur.copy())
                return
            
            if i < len(nums) and val + nums[i] <= target:
                cur.append(nums[i])
                backtrack(cur, i, val + nums[i])

                cur.pop()
                backtrack(cur, i + 1, val)

            return

        backtrack([], 0, 0)
        return res


def main():

    solution = Solution()

    nums = [2, 5, 6, 9]
    target = 9
    print(f"The set of numbers that make {target} are {solution.combinationSum(nums, target)}")

    nums = [3, 4, 5]
    target = 16
    print(f"The set of numbers that make {target} are {solution.combinationSum(nums, target)}")

    nums = [3]
    target = 5
    print(f"The set of numbers that make {target} are {solution.combinationSum(nums, target)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 15-11-2024
"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def backtrack(i, cur):
            if i == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            backtrack(i + 1, cur)
            cur.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, cur)

        backtrack(0, [])
        return res


def main():

    solution = Solution()

    nums = [1, 2, 1]
    print(f"The combinations of {nums} are {solution.subsetsWithDup(nums)}")

    nums = [7, 7]
    print(f"The combinations of {nums} are {solution.subsetsWithDup(nums)}")

    return None


if __name__ == "__main__":
    main()

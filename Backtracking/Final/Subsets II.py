"""
Difficulty : Medium 
Date created : 26-11-2024
"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        res = []
        cur = []
        nums.sort()

        def backtrack(i):

            if i == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            backtrack(i + 1)
            cur.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res


def main():

    solution = Solution()

    nums = [1, 2, 1]
    print(f"The possible subsets of {nums} are \n{solution.subsetsWithDup(nums)}\n")

    nums = [7, 7]
    print(f"The possible subsets of {nums} are \n{solution.subsetsWithDup(nums)}\n")

    return None


if __name__ == "__main__":
    main()

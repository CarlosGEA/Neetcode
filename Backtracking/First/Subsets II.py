"""
Difficulty : Medium 
Date created : 08-11-2024
"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = set()

        def dfs(i, cur):

            if i >= len(nums):
                res.add(tuple(cur))

                return

            cur.append(nums[i])
            dfs(i + 1, cur)

            cur.pop()
            dfs(i + 1, cur)

        nums.sort()
        dfs(0, [])
        return [list(sub) for sub in res]


def main():

    solution = Solution()

    nums = [1, 2, 1]
    print(f"The possible subsets of {nums} are \n{solution.subsetsWithDup(nums)}\n")

    nums = [7, 7]
    print(f"The possible subsets of {nums} are \n{solution.subsetsWithDup(nums)}\n")

    return None


if __name__ == "__main__":
    main()

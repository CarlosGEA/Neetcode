"""
Difficulty : Medium
Date created : 11-11-2024
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(i, cur):

            if i >= len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            backtrack(i + 1, cur)

            cur.pop()
            backtrack(i + 1, cur)

            return

        backtrack(0, [])
        return res


def main():

    solution = Solution()

    nums = [1, 2, 3]
    print(f"The subsets of {nums} are {solution.subsets(nums)}")

    nums = [7]
    print(f"The subsets of {nums} are {solution.subsets(nums)}")
    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 11-11-2024
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # res = []

        def backtrack(i, res):

            if i >= len(nums):
                return res

            res = backtrack(i + 1, res)
            new_res = []
            for perm in res:
                for p in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(p, nums[i])
                    new_res.append(perm_copy)

            return new_res

        return backtrack(0, [[]])


def main():

    solution = Solution()

    nums = [1, 2, 3]
    print(f"The permutations of nums are {solution.permute(nums)}")

    nums = [7]
    print(f"The permutations of nums are {solution.permute(nums)}")

    return None


if __name__ == "__main__":
    main()

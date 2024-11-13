"""
Difficulty : Medium
Date created : 12-11-2024
"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = [[]]
        prev_idx = idx = 0
        for i in range(len(nums)):
            idx = prev_idx if i >= 1 and nums[i] == nums[i - 1] else 0
            prev_idx = len(res)
            for j in range(idx, prev_idx):
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)
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

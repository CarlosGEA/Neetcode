"""
Difficulty : Medium
Date created : 07-11-2024
"""

from collections import defaultdict


class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:

        curr = defaultdict(list)
        for num in nums:

            curr[num].append([num])

            new_dict = dict(curr)
            while new_dict:
                changed_dict = defaultdict(list)
                for valsum, combs in new_dict.items():
                    if num + valsum <= target:
                        for comb in combs:
                            curr[num + valsum].append(comb + [num])
                            changed_dict[num + valsum].append(comb + [num])
                new_dict = dict(changed_dict)

        return [list(item) for item in set(tuple(comb) for comb in curr[target])]



def main():

    solution = Solution()

    nums = [2, 5, 6, 9]
    target = 9
    print(
        f"The combination of numbers to make {target} are {solution.combinationSum(nums, target)}"
    )

    nums = [3, 4, 5]
    target = 16
    print(
        f"The combination of numbers to make {target} are {solution.combinationSum(nums, target)}"
    )

    nums = [3]
    target = 5
    print(
        f"The combination of numbers to make {target} are {solution.combinationSum(nums, target)}"
    )

    return None


if __name__ == "__main__":
    main()

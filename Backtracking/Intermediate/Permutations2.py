"""
Difficulty : Medium
Date created : 14-11-2024
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # use same function to backtrack but similar method as to before

        self.res = [[]]

        if not nums:
            return
        
        self.permute(nums[1:])
        num = nums[0]
        tmp = []

        for comb in self.res:
            for i in range(len(comb) + 1):
                comb_copy = comb.copy()
                comb_copy.insert(i, num)
                tmp.append(comb_copy)

        self.res = tmp

        return self.res


def main():

    solution = Solution()

    nums = [1, 2, 3]
    print(f"The possible permutations of {nums} are : {solution.permute(nums)}")

    nums = [7]
    print(f"The possible permutations of {nums} are : {solution.permute(nums)}")

    return None


if __name__ == "__main__":
    main()

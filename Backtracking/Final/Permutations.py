"""
Difficulty : Medium 
Date created : 26-11-2024
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        if not nums:
            return [[]]
        
        cur = self.permute(nums[1:])
        res = []

        for perm in cur:
            for idx in range(len(nums)):
                perm_copy = perm.copy()
                perm_copy.insert(idx, nums[0]) 
                res.append(perm_copy)     

        return res
def main():

    solution = Solution()

    nums = [1, 2, 3]
    print(f"The permutations of {nums} are \n{solution.permute(nums)}\n")

    nums = [7]
    print(f"The permutations of {nums} are \n{solution.permute(nums)}\n")

    return None


if __name__ == "__main__":
    main()

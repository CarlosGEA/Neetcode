"""
Difficulty : Medium 
Date created : 08-11-2024
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def dfs(i, cur):

            if i == len(nums):
                return cur
            new_cur = []

            for p in cur:
                for j in range(i + 1):
                    p.insert(j, nums[i])
                    new_cur.append(p.copy())
                    p.pop(j)

            return dfs(i + 1, new_cur)

        return dfs(0, [[]])


def main():

    solution = Solution()

    nums = [1, 2, 3]
    print(f"The permutations of {nums} are \n{solution.permute(nums)}\n")

    nums = [7]
    print(f"The permutations of {nums} are \n{solution.permute(nums)}\n")

    return None


if __name__ == "__main__":
    main()

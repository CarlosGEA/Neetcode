"""
Difficulty : Medium
Date created : 18-10-2024
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()

        snums = sorted(nums)
        for l in range(len(snums) - 2):
            r = len(nums) - 1
            m = l + 1
            while m < r:
                val = snums[l] + snums[m] + snums[r]
                if val == 0:
                    res.add(tuple([snums[l], snums[m], snums[r]]))
                    m += 1
                elif val < 0:
                    m += 1
                else:
                    r -= 1
        
        return [list(r) for r in res]


def main():

    solution = Solution()

    nums = [-1, 0, 1, 2, -1, -4]
    print(f"The possible triplets that sum to 0 are {solution.threeSum(nums)}")

    nums = [0, 1, 1]
    print(f"The possible triplets that sum to 0 are {solution.threeSum(nums)}")

    nums = [0, 0, 0, 0]
    print(f"The possible triplets that sum to 0 are {solution.threeSum(nums)}")

    return None


if __name__ == "__main__":
    main()

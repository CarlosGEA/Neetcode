"""
Difficulty : Medium
Date created : 31-10-2024
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        res = set()
        nums.sort()

        for i, num in enumerate(nums):

            l = i + 1
            r = len(nums) - 1

            while l < r:
                numsum = num + nums[l] + nums[r]
                if numsum == 0:
                    res.add(tuple([nums[l], num, nums[r]]))

                if numsum > 0:
                    r -= 1
                else:
                    l += 1

        return [list(i) for i in res]


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

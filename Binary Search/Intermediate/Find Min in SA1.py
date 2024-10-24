"""
Difficulty : Medium 
Date created : 23-10-2024
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1

        res = float("inf")

        while l < r:
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            # elif nums[m] < nums[l]:
            #     l += 1
            else:
                r = m - 1

        return min(res, nums[l])


def main():

    solution = Solution()

    nums = [3, 4, 5, 6, 1, 2]
    print(f"The minimum in this array is {solution.findMin(nums)}")

    nums = [4, 5, 0, 1, 2, 3]
    # nums = [5, 1, 2, 3, 4]
    print(f"The minimum in this array is {solution.findMin(nums)}")

    nums = [4, 5, 6, 7]
    print(f"The minimum in this array is {solution.findMin(nums)}")

    return None


if __name__ == "__main__":
    main()

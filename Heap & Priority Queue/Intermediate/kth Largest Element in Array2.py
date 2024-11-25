"""
Difficulty : Medium
Date created : 25-11-2024
"""


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        k = len(nums) - k

        def pivot(l, r):

            p = nums[r]
            for n in range(l, len(nums)):

                if nums[n] < p:
                    nums[l], nums[n] = nums[n], nums[l]
                    l += 1

            nums[r], nums[l] = nums[l], nums[r]

            if l == k:
                return nums[k]

            elif l < k:
                return pivot(l + 1, r)

            else:
                return pivot(0, l - 1)

        return pivot(0, len(nums) - 1)


def main():

    solution = Solution()

    nums = [1]  # [2, 3, 1, 5, 4]
    k = 1  # 2
    print(f"The {k}th largest element is {solution.findKthLargest(nums, k)}")

    nums = [2, 3, 1, 1, 5, 5, 4]
    k = 3
    print(f"The {k}th largest element is {solution.findKthLargest(nums, k)}")

    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(f"The {k}th largest element is {solution.findKthLargest(nums, k)}")

    return None


if __name__ == "__main__":
    main()

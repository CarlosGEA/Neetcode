"""
Difficulty : Medium
Date created : 20-11-2024
"""


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # New attempt with quick sort
        k = len(nums) - k

        def quickSelect(l, r):

            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)

            elif p < k:
                return quickSelect(p + 1, r)

            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)


def main():

    solution = Solution()

    nums = [2, 3, 1, 5, 4]
    k = 2
    print(f"The {k}th largest element in {nums} is {solution.findKthLargest(nums, k)}")

    nums = [2, 3, 1, 1, 5, 5, 4]
    k = 3
    print(f"The {k}th largest element in {nums} is {solution.findKthLargest(nums, k)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 04-12-2024
"""


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k

        def search(l, r):

            p = l
            pivot = nums[r]

            for n in range(l, r):
                if nums[n] <= pivot:
                    nums[n], nums[p] = nums[p], nums[n]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]
            if k < p:
                return search(l, p - 1)

            elif k > p:
                return search(p + 1, r)

            else:
                return nums[k]

        return search(0, len(nums) - 1)


def main():

    solution = Solution()

    nums = [2, 3, 1, 5, 4]
    k = 2
    print(f"The {k}th largest element in nums is {solution.findKthLargest(nums, k)}")

    nums = [2, 3, 1, 1, 5, 5, 4]
    k = 3
    print(f"The {k}th largest element in nums is {solution.findKthLargest(nums, k)}")

    return None


if __name__ == "__main__":
    main()

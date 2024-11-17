"""
Difficulty : Medium
Date created : 17-11-2024
"""

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Without sorting :

        res = []
        heapq.heapify(res)

        for n in nums:
            heapq.heappush(res, n)
            if len(res) > k:
                heapq.heappop(res)

        return res[0]

        # return sorted(nums)[-k]


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

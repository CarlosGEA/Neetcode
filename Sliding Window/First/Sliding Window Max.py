"""
Difficulty : Hard
Date created : 25-10-2024
"""


# Complexity -- Time: O(n * k), Space: O(n - k)
# n - len(nums)
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        res = []
        max_w = max(nums[:k])

        left = 0

        for idx in range(k - 1, len(nums)):

            if nums[left - 1] == max_w:
                max_w = max(nums[left : idx + 1])
            else:
                max_w = max(max_w, nums[idx])
            res.append(max_w)
            left += 1
        return res


def main():

    solution = Solution()

    nums = [1, 2, 1, 0, 4, 2, 6]
    k = 3
    print(
        f"The maximum elements in each window of size {k} is {solution.maxSlidingWindow(nums, k)}"
    )

    return None


if __name__ == "__main__":
    main()

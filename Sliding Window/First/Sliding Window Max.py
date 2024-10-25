"""
Difficulty : Hard
Date created : 25-10-2024
"""


# Complexity -- Time: O(n), Space: O(k)
# n - len(nums)
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        res = []
        stack = []

        for i in range(k - 1):
            while stack and stack[-1] < nums[i]:
                stack.pop()
            stack.append(nums[i])

        left = 0
        for idx in range(k - 1, len(nums)):

            if left > 0 and nums[left - 1] == stack[0]:
                del stack[0]

            while stack and stack[-1] < nums[idx]:
                stack.pop()
            stack.append(nums[idx])

            res.append(stack[0])
            left += 1

        return res


def main():

    solution = Solution()

    # nums = [1, 2, 1, 0, 4, 2, 6]
    # k = 3
    # print(
    #     f"The maximum elements in each window of size {k} is {solution.maxSlidingWindow(nums, k)}"
    # )

    nums = [-7, -8, 7, 5, 7, 1, 6, 0]
    k = 4
    print(
        f"The maximum elements in each window of size {k} is {solution.maxSlidingWindow(nums, k)}"
    )

    return None


if __name__ == "__main__":
    main()

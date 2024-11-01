"""
Difficulty : Hard
Date created : ??-11-2024
"""


# Complexity -- Time: O(n), Space: O(k)
# n - len(nums)
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        stack = []  # number, index
        res = []

        l = 0
        for r, n in enumerate(nums):

            while stack and stack[-1][0] < n:
                stack.pop()

            stack.append([n, r])

            if len(stack) > 1 and stack[0][1] < l:
                stack.pop(0)

            if r >= k - 1:

                res.append(stack[0][0])
                l += 1

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

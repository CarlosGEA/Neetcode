"""
Difficulty : Hard
Date created : 04-11-2024
"""


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        stack = []
        res = []
        for idx, num in enumerate(nums):
            while stack and num > stack[-1][0]:
                stack.pop()

            stack.append([num, idx])

            if idx - stack[0][1] >= k:
                stack.pop(0)

            if idx >= k - 1:
                res.append(stack[0][0])

        return res


def main():

    solution = Solution()

    nums = [1, 2, 1, 0, 4, 2, 6]
    k = 3
    print(
        f"The maximum elements in each window of size {k} is {solution.maxSlidingWindow(nums, k)}"
    )

    nums = [-7, -8, 7, 5, 7, 1, 6, 0]
    k = 4
    print(
        f"The maximum elements in each window of size {k} is {solution.maxSlidingWindow(nums, k)}"
    )

    return None


if __name__ == "__main__":
    main()

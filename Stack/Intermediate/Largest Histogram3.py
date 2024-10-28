"""
Difficulty : Hard
Date created : 27-10-2024
"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        stack = []
        indices = []
        res = 0
        for idx, h in enumerate(heights):

            start = idx

            while stack and h <= stack[-1]:
                res = max(res, stack[-1] * (idx - indices[-1]))
                stack.pop()
                start = indices.pop()

            stack.append(h)
            indices.append(start)

        for i in range(len(stack)):
            res = max(res, stack[i] * (len(heights) - indices[i]))

        return res


def main():

    solution = Solution()

    heights = [7, 1, 7, 2, 2, 4]
    # heights = [1]
    print(f"The largest rectangle area is {solution.largestRectangleArea(heights)}")

    heights = [1, 3, 7]
    print(f"The largest rectangle area is {solution.largestRectangleArea(heights)}")

    return None


if __name__ == "__main__":
    main()

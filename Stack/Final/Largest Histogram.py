"""
Difficulty : Hard
Date created : 30-10-2024
"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):

            nidx = i
            while stack and h <= stack[-1][0]:
                newh, idx = stack.pop()
                res = max(res, newh * (i - idx))
                nidx = idx

            stack.append([h, nidx])

        for h, i in stack:
            res = max(res, h * (len(heights) - i))

        return res


def main():

    solution = Solution()

    heights = [7, 1, 7, 2, 2, 4]
    print(
        f"The largest rectangle area that can be made is {solution.largestRectangleArea(heights)}"
    )

    heights = [1, 3, 7]
    print(
        f"The largest rectangle area that can be made is {solution.largestRectangleArea(heights)}"
    )

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Hard
Date created : 24-10-2024
"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        res = 0
        stack = []
        idx = []

        for i, h in enumerate(heights):
            if not stack or h >= stack[-1]:
                stack.append(h)
                idx.append(i)

            else:
                while stack and h < stack[-1]:
                    res = max(res, h * (i - idx[-1]))
                    stack.pop()
                    nidx = idx.pop()

                stack.append(h)
                idx.append(nidx)

        for i in range(len(stack)):
            res = max(res, stack[i] * (len(heights) - idx[i]))
    
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

"""
Difficulty : Hard
Date created : 17-10-2024
"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Make way more efficient with stacks
        max_area = 0
        n = len(heights)

        for h in range(n):
            max_h_area = heights[h]
            min_h = heights[h]
            for h2 in range(h + 1, n):
                min_h = min(min_h, heights[h2])
                max_h_area = max(max_h_area, min_h * (h2 + 1 - h))
            max_area = max(max_area, max_h_area)
        return max_area


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

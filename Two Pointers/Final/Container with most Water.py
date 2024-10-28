"""
Difficulty : Medium
Date created : 28-10-2024
"""


class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l = 0
        r = len(heights) - 1

        res = 0

        while l < r:

            if heights[l] < heights[r]:
                res = max(res, heights[l] * (r - l))
                l += 1

            else:
                res = max(res, heights[r] * (r - l))
                r -= 1

        return res


def main():

    solution = Solution()

    height = [1, 7, 2, 5, 4, 7, 3, 6]
    print(f"The max area of water for {height} is {solution.maxArea(height)}")

    height = [2, 2, 2]
    print(f"The max area of water for {height} is {solution.maxArea(height)}")

    return None


if __name__ == "__main__":
    main()

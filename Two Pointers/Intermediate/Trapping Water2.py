"""
Difficulty : Hard
Date created : 24-10-2024
"""


class Solution:
    def trap(self, height: list[int]) -> int:

        l = 0
        r = len(height) - 1
        area = 0

        maxl = height[0]
        maxr = height[r]

        while l < r:

            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                area += maxl - height[l]

            else:
                r -= 1
                maxr = max(maxr, height[r])
                area += maxr - height[r]

        return area


def main():
    solution = Solution()

    height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    print(f"The max amount of water trapped is {solution.trap(height)}")
    return None


if __name__ == "__main__":
    main()

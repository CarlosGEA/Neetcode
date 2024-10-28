"""
Difficulty : Hard
Date created : 28-10-2024
"""


class Solution:
    def trap(self, height: list[int]) -> int:

        if not height: return 0

        l = 0
        r = len(height) - 1

        maxl = height[l]
        maxr = height[r]

        area = 0
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

    # height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height = [4, 2, 0, 3, 2, 5]

    print(f"The maximum amount of water that can be trapped is {solution.trap(height)}")

    # height = [4, 2, 3]
    height = [5, 4, 1, 2]
    height = []
    print(f"The maximum amount of water that can be trapped is {solution.trap(height)}")

    return None


if __name__ == "__main__":
    main()

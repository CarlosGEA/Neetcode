"""
Difficulty : Hard
Date created : 21-10-2024
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0

        maxl = height[r]
        maxr = height[l]

        while l < r:
            if maxl < maxr:
                l += 1
                res += max(0, maxl - height[l])
                maxl = max(maxl, height[l])
            else:
                r -= 1
                res += max(0, maxr - height[r])
                maxr = max(maxr, height[r])

        return res


def main():

    solution = Solution()

    height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    print(f"The max amount of water trapped is {solution.trap(height)}")

    return None


if __name__ == "__main__":
    main()

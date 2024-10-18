"""
Difficulty : Hard
Date created : 18-10-2024
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        area = 0
        l = 0

        stack = []
        while l < len(height) - 1:

            while not stack and l < len(height) - 1 and height[l] < height[l + 1]:
                l += 1
            r = l

            while not stack or (r < len(height) - 1 and stack[-1][0] >= height[r]):
                stack.append([height[r], r])
                r += 1

                while height[r] > stack[-1][0] and len(stack) > 1:
                    area += (r - stack[-2][1] - 1) * (min(height[r], stack[-2][0]) - stack[-1][0])
                    stack.pop()

            if r == len(height) - 1:
                break

            if len(stack) == 1:
                stack.pop()
                l = r
        return area


def main():

    solution = Solution()

    # height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height = [4, 2, 0, 3, 2, 5]

    print(f"The maximum amount of water that can be trapped is {solution.trap(height)}")

    height = [4, 2, 3]
    height = [5, 4, 1, 2]
    print(f"The maximum amount of water that can be trapped is {solution.trap(height)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Hard
Date created : 14-01-2025
New attempt :
"""


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:

        return

def main():

    solution = Solution()

    grid = [[0, 1], [2, 3]]
    print(
        f"Starting in the top left corner, to reach the bottom right corner takes {solution.swimInWater(grid)} times."
    )

    grid = [[0, 1, 2, 10], [9, 14, 4, 13], [12, 3, 8, 15], [11, 5, 7, 6]]
    print(
        f"Starting in the top left corner, to reach the bottom right corner takes {solution.swimInWater(grid)} times."
    )

    grid = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6],
    ]

    return None


if __name__ == "__main__":
    main()

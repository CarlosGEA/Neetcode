"""
Difficulty : Medium
Date created : -12-2024
"""


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # same as last time, nearly fully right
       
        return


def main():
    solution = Solution()

    edges = [[9, 10], [5, 8], [2, 6], [1, 5], [3, 8], [4, 9], [8, 10], [4, 10], [6, 8], [7, 9]]
    print(f"The redundant connection is {solution.findRedundantConnection(edges)}")

    edges = [[1, 2], [1, 3], [3, 4], [2, 4]]
    print(f"The redundant connection is {solution.findRedundantConnection(edges)}")

    edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
    print(f"The redundant connection is {solution.findRedundantConnection(edges)}")

    return None


if __name__ == "__main__":
    main()

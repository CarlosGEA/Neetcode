"""
Difficulty : Medium
Date created : 02-12-2024
New attempt :
"""


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        return
  

def main():

    solution = Solution()

    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(f"These edges from a valid graph? : {solution.validTree(n, edges)}")

    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(f"These edges from a valid graph? : {solution.validTree(n, edges)}")

    n = 5
    edges = [[0, 1], [2, 1], [3, 2], [3, 1], [4, 1]]
    print(f"These edges from a valid graph? : {solution.validTree(n, edges)}")

    return None


if __name__ == "__main__":
    main()

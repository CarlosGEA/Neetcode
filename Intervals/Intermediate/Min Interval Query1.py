"""
Difficulty : Hard
Date created : 17-12-2024
New attempt : 
"""

from collections import defaultdict


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:

        return 


def main():

    solution = Solution()

    intervals = [[1, 3], [2, 3], [3, 7], [6, 6]]
    queries = [2, 3, 1, 7, 6, 8]
    print(f"The shortest interval for each query is {solution.minInterval(intervals, queries)}")

    return None


if __name__ == "__main__":
    main()

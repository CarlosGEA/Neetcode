"""
Difficulty : Medium
Date created : 15-01-2025
"""

import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        return math.factorial(m + n) // (math.factorial(m) * math.factorial(n))


def main():

    solution = Solution()

    m = 3
    n = 6
    print(
        f"The number of unique paths to reach the bottom right from top left {m}x{n} grid is {solution.uniquePaths(m, n)}"
    )

    m = 3
    n = 3
    print(
        f"The number of unique paths to reach the bottom right from top left {m}x{n} grid is {solution.uniquePaths(m, n)}"
    )

    return None


if __name__ == "__main__":
    main()

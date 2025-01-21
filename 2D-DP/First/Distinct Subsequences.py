"""
Difficulty : Hard
Date created : 21-01-2025
"""

from collections import defaultdict


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def dfs(i, j):
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            cur = 0
            if s[i] == t[j]:
                cur += dfs(i + 1, j + 1)
            
            cur += dfs(i + 1, j)
            

            return cur

        return dfs(0, 0)


def main():

    solution = Solution()

    s = "caaat"
    t = "cat"
    print(
        f"The number of distinct subsequences of {s} which are equal to {t} are {solution.numDistinct(s, t)}"
    )

    s = "xxyxy"
    t = "xy"
    print(
        f"The number of distinct subsequences of {s} which are equal to {t} are {solution.numDistinct(s, t)}"
    )

    return None


if __name__ == "__main__":
    main()

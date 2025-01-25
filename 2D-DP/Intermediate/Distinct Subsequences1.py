"""
Difficulty : Hard
Date created : 24-01-2025
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # non recursive solution
        # caching i, j pair
        memo = {}

        def dfs(i, j):
            if j >= len(t):
                return 1

            if i >= len(s):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            memo[(i, j)] = res
            return res

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

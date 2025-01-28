"""
Difficulty : Hard
Date created : 22-01-2025
New attempt : 25-01-2025
New attempt : 
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        '.' Matches any single character
        '*' Matches zero or more of the preceding element.
        """

        memo = {}

        def dfs(i, j):

            if j == len(p):
                return i == len(s)

            if (i, j) in memo:
                return memo[(i, j)]

            matches = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                memo[(i, j)] = dfs(i, j + 2) or (matches and dfs(i + 1, j))
                return memo[(i, j)]

            if matches:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = False
            return memo[(i, j)]

        return dfs(0, 0)


def main():

    solution = Solution()

    s = "aa"
    p = ".b"
    print(f"The pattern {p} matches expression {s}? : {solution.isMatch(s, p)}")

    s = "nnn"
    p = "n*"
    print(f"The pattern {p} matches expression {s}? : {solution.isMatch(s, p)}")

    s = "xyz"
    p = ".*z"
    print(f"The pattern {p} matches expression {s}? : {solution.isMatch(s, p)}")

    return None


if __name__ == "__main__":
    main()

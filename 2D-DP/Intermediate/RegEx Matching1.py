"""
Difficulty : Hard
Date created : 31-01-2025
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # move j along until the end

        # check if it matches, if it has the star next, check either use or not use the things
        # otherwise if it matches, check next along
        # otherwise just return false

        cache = {}

        def dfs(i, j):
            if j == len(p):
                return i == len(s)

            if (i, j) in cache:
                return cache[(i, j)]

            matches = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or (matches and dfs(i + 1, j))
                return cache[(i, j)]
            if matches:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            cache[(i, j)] = False

            return cache[(i, j)]

        return dfs(0, 0)


def main():

    solution = Solution()

    # s = "aa"
    # p = ".b"
    # print(f"The pattern {p} matches expression {s}? : {solution.isMatch(s, p)}")

    # s = "nnn"
    # p = "n*"
    # print(f"The pattern {p} matches expression {s}? : {solution.isMatch(s, p)}")

    s = "xyz"
    p = ".*z"
    print(f"The pattern {p} matches expression {s}? : {solution.isMatch(s, p)}")

    return None


if __name__ == "__main__":
    main()

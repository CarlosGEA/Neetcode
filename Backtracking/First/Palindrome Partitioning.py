"""
Difficulty : Medium
Date created : 10-11-2024
New attempt : 14-11-2024
New attempt : 17-11-2024
"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def backtrack(part, i):

            if i == len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPal(s, i, j):
                    part.append(s[i : j + 1])
                    backtrack(part, j + 1)
                    part.pop()

        backtrack([], 0)
        return res

    def isPal(self, s, l, r):

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


def main():

    solution = Solution()

    s = "aab"
    print(f"The possible palindromes of {s} are {solution.partition(s)}")

    s = "a"
    print(f"The possible palindromes of {s} are {solution.partition(s)}")

    s = "cdd"
    print(f"The possible palindromes of {s} are {solution.partition(s)}")

    return None


if __name__ == "__main__":
    main()

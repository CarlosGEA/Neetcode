"""
Difficulty : Hard
Date created : 04-11-2024
"""

from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        charS = defaultdict(int)
        charT = defaultdict(int)
        for c in t:
            charT[c] += 1

        res = ""
        minres = float("inf")

        l = 0
        matches = 0
        for r, c in enumerate(s):
            charS[c] += 1

            if c in charT and charS[c] == charT[c]:
                matches += 1

            while matches == len(charT):
                if r - l + 1 < minres:
                    res = s[l : r + 1]
                    minres = r - l + 1

                charS[s[l]] -= 1
                if s[l] in charT and charS[s[l]] == charT[s[l]] - 1:
                    matches -= 1
                l += 1

        return res


def main():

    solution = Solution()

    s = "OUZODYXAZV"
    t = "XYZ"
    print(f"The smallest substring of s containing all elements of t is {solution.minWindow(s, t)}")

    s = "xyz"
    t = "xyz"
    print(f"The smallest substring of s containing all elements of t is {solution.minWindow(s, t)}")

    s = "x"
    t = "xy"
    print(f"The smallest substring of s containing all elements of t is {solution.minWindow(s, t)}")

    return None


if __name__ == "__main__":
    main()

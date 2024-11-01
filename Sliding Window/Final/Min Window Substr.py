"""
Difficulty : Hard
Date created : -11-2024
"""


# Complexity -- Time: O(n  * m), Space: O(m)
# n - len(s), m - len(t)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""

        if len(t) > len(s):
            return res

        charMapT = {}
        charMapS = {}

        for c in range(len(t)):
            charMapT[t[c]] = charMapT.get(t[c], 0) + 1

        matches = 0
        minres = float("inf")
        l = 0
        for i in range(len(s)):

            charMapS[s[i]] = charMapS.get(s[i], 0) + 1
            if s[i] in charMapT:
                if charMapS[s[i]] == charMapT[s[i]]:
                    matches += 1

            while matches == len(charMapT) and l <= i:
                if i - l + 1 < minres:
                    res = s[l : i + 1]
                    minres = i - l + 1
                charMapS[s[l]] -= 1
                if s[l] in charMapT and charMapS[s[l]] + 1 == charMapT[s[l]]:
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

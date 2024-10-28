"""
Difficulty : Hard
Date created : 27-10-2024
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        Tcount = {}
        for c in t:
            Tcount[c] = 1 + Tcount.get(c, 0)

        l = 0
        matched = 0
        Scount = {}

        reslen = float("inf")
        res = ""
        for r, c in enumerate(s):

            Scount[c] = 1 + Scount.get(c, 0)
            
            if c in Tcount:
                if Scount[c] == Tcount[c]:
                    matched += 1

            while matched == len(Tcount):
                if r - l + 1 < reslen:
                    reslen = r - l + 1
                    res = s[l : r + 1]

                Scount[s[l]] -= 1
                if s[l] in Tcount and Scount[s[l]] == Tcount[s[l]] - 1:
                    matched -= 1
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

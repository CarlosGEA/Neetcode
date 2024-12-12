"""
Difficulty : Medium
Date created : 12-12-2024
"""

from collections import defaultdict


class Solution:
    def numDecodings(self, s: str) -> int:
        seenMap = defaultdict(int)

        def dfs(i):
            if i == len(s):
                return 1

            if i in seenMap:
                return seenMap[i]

            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            seenMap[i] = res
            return res

        return dfs(0)


def main():

    solution = Solution()

    s = "12"
    print(f"The possible number of decodings is {solution.numDecodings(s)}")

    s = "01"
    print(f"The possible number of decodings is {solution.numDecodings(s)}")

    s = "10"
    print(f"The possible number of decodings is {solution.numDecodings(s)}")

    return None


if __name__ == "__main__":
    main()

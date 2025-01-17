"""
Difficulty : Medium
Date created : 18-01-2025
"""


class Solution:
    def numDecodings(self, s: str) -> int:

        res = 0

        def dfs(i):
            nonlocal res
            if i == len(s):
                res += 1
                return 1

            if s[i] == "0":
                return

            dfs(i + 1)
            
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                dfs(i + 2)
            return

        dfs(0)
        return res


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

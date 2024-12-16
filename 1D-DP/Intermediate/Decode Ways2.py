"""
Difficulty : Medium
Date created : 16-12-2024
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        # good, try bottom up, work backwards so no dict is needed

        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                continue

            dp[i] += dp[i + 1]

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]

        return dp[0]


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

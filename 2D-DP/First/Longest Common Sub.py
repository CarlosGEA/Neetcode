"""
Difficulty : Medium
Date created : 16-01-2025
New attempt : 19-01-2025
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # visualise grid -> 2 for loops work backwards -> then space optimise further

        if len(text1) > len(text2):
            text2, text1 = text1, text2

        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):

                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i + 1][j + 1])

                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


def main():

    solution = Solution()

    text1 = "cat"
    text2 = "crabt"
    print(
        f"The longest common substring of {text1} and {text2} is {solution.longestCommonSubsequence(text1, text2)}"
    )
    text1 = "abcd"
    text2 = "abcd"
    print(
        f"The longest common substring of {text1} and {text2} is {solution.longestCommonSubsequence(text1, text2)}"
    )

    text1 = "abcd"
    text2 = "efgh"
    print(
        f"The longest common substring of {text1} and {text2} is {solution.longestCommonSubsequence(text1, text2)}"
    )

    return None


if __name__ == "__main__":
    main()

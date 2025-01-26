"""
Difficulty : Medium
Date created : 22-01-2025
New attempt : 25-01-2025
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if len(text1) > len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)
        for i in range(len(text1) - 1, -1, -1):
            prev = 0
            for j in range(len(text2) - 1, -1, -1):
                tmp = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                prev = tmp

        return dp[0]


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

"""
Difficulty : Medium
Date created : 16-01-2025
New attempt : 
"""

from collections import defaultdict


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        return

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

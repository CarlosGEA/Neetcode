"""
Difficulty : Medium
Date created : -12-2024
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # iterate over string and word rather than string twice
        return 

def main():

    solution = Solution()

    s = "neetcode"
    wordDict = ["neet", "code"]
    print(f"The word can be segmented using the dict : {solution.wordBreak(s, wordDict)}")

    s = "applepenapple"
    wordDict = ["apple", "pen", "ape"]
    print(f"The word can be segmented using the dict : {solution.wordBreak(s, wordDict)}")

    s = "catsincars"
    wordDict = ["cats", "cat", "sin", "in", "car"]
    print(f"The word can be segmented using the dict : {solution.wordBreak(s, wordDict)}")

    return None


if __name__ == "__main__":
    main()

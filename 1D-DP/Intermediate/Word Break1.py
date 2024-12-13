"""
Difficulty : Medium
Date created : 13-12-2024
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # cache if can reach current position, iterate backwards
        res = [False] * len(s)
        res.append(True)
        wordSet = set(wordDict)
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                # print(s[i:j+1])
                if s[i:j+1] in wordSet and res[j+1] == True:
                    res[i] = True

        return res[0]


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

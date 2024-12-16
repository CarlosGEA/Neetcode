"""
Difficulty : Medium
Date created : 16-12-2024
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        res = [False] * len(s)
        res.append(True)

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word) <= len(s)) and s[i: i + len(word)] == word:
                    res[i] = res[i + len(word)  ]
                    
                if res[i]:
                    break

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

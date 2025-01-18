"""
Difficulty : Medium
Date created : 18-01-2025
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        res = [False] * len(s)
        res.append(True)

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    res[i] |= res[i + len(word)]

        return res[0]


def main():

    solution = Solution()

    s = "aaaaaaa"
    wordDict = ["aaaa", "aaa"]
    print(f"The string can be split into dictionary values : {solution.wordBreak(s, wordDict)}")

    s = "applepenapple"
    wordDict = ["apple", "pen", "ape"]
    print(f"The string can be split into dictionary values : {solution.wordBreak(s, wordDict)}")

    s = "catsincars"
    wordDict = ["cats", "cat", "sin", "in", "car"]
    print(f"The string can be split into dictionary values : {solution.wordBreak(s, wordDict)}")

    s="abcd"
    wordDict=["a","abc","b","cd"]
    print(f"The string can be split into dictionary values : {solution.wordBreak(s, wordDict)}")


    return None


if __name__ == "__main__":
    main()

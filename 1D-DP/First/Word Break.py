"""
Difficulty : Medium
Date created : 10-12-2024
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # splits = []
        # cur = []

        smallest = len(min(wordDict, key=len))

        def dfs(i):
            if i == len(s):
                # splits.append(cur.copy())
                return True

            for j in range(i + smallest - 1, len(s)):
                if s[i : j + 1] in wordDict:
                    # cur.append(s[i : j + 1])
                    if dfs(j + 1):
                        return True
                    # cur.pop()

            return False

        return dfs(0)
        # return len(splits) != 0


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

    return None


if __name__ == "__main__":
    main()

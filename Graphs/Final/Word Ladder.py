"""
Difficulty : Hard
Date created : 15-01-2025
"""

from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        patternDict = defaultdict(set)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                patternDict[pattern].add(word)

        queue = deque([beginWord])
        res = 0
        seen = set()
        while queue:
            res += 1

            for _ in range(len(queue)):
                check = queue.popleft()

                if check == endWord:
                    return res
                if check in seen:
                    continue
                seen.add(check)
                for i in range(len(check)):
                    pattern = check[:i] + "*" + check[i + 1 :]
                    queue += patternDict[pattern]

        return 0


def main():

    solution = Solution()

    beginWord = "cat"
    endWord = "sag"
    wordList = ["bat", "bag", "sag", "dag", "dot"]
    print(
        f"The mininum number of steps to get from {beginWord} to {endWord} is {solution.ladderLength(beginWord, endWord, wordList)}"
    )

    beginWord = "cat"
    endWord = "sag"
    wordList = ["bat", "bag", "sat", "dag", "dot"]
    print(
        f"The mininum number of steps to get from {beginWord} to {endWord} is {solution.ladderLength(beginWord, endWord, wordList)}"
    )

    return None


if __name__ == "__main__":
    main()

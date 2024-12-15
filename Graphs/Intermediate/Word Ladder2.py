"""
Difficulty : Hard
Date created : 15-12-2024
"""

from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        patternDict = defaultdict(list)
        queue = deque([beginWord])

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                patternDict[pattern].append(word)

        seen = set()
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return count

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1 :]
                    for newWord in patternDict[pattern]:
                        if newWord not in seen:
                            seen.add(newWord)
                            queue.append(newWord)

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

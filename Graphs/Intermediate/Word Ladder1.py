"""
Difficulty : Hard
Date created : 11-12-2024
"""

from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        patternDict = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]  # check this
                patternDict[pattern].add(word)

        queue = deque([beginWord])
        count = 0
        seen = set()
        while queue:
            count += 1

            for i in range(len(queue)):
                word = queue.popleft()
                seen.add(word)

                if word == endWord:
                    return count

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for next_word in patternDict[pattern]:
                        if next_word not in seen:
                            queue.append(next_word)

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

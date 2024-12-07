"""
Difficulty : Hard
Date created : 07-12-2024
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        def dfs(cur, count):
            nonlocal min_count

            if cur == endWord:
                min_count = min(count + 1, min_count)
                return count

            seen.add(cur)
            for word in wordList:
                if word not in seen and self.share(word, cur):
                    dfs(word, count + 1)
            seen.remove(cur)
            return 0

        seen = set()

        min_count = float("inf")
        dfs(beginWord, 0)
        
        return min_count if min_count != float("inf") else 0

    def share(self, word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1

        return diff == 1


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

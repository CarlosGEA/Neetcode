"""
Difficulty : Medium
Date created : 22-01-2025
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}  # store (i, j)

        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            elif i == len(word1):
                return 1 + dfs(i, j + 1) # just insert
            elif j == len(word2):
                return 1 + dfs(i + 1, j) # just remove

            if (i, j) in memo:
                return memo[(i, j)]

            cur = float("inf")

            if word1[i] == word2[j]:
                cur = min(cur, dfs(i + 1, j + 1))

            cur = min(cur, 1 + dfs(i + 1, j))  # remove ith element
            cur = min(cur, 1 + dfs(i, j + 1))  # insert ith element
            cur = min(cur, 1 + dfs(i + 1, j + 1))  # replace ith element

            memo[(i, j)] = cur
            return cur

        return dfs(0, 0)


def main():

    solution = Solution()

    word1 = "monkeys"
    word2 = "money"
    print(
        f"The minimum number of operations to turn {word1} into {word2} by only replacing, inserting or removing letters is {solution.minDistance(word1, word2)}"
    )

    word1 = "neatcdee"
    word2 = "neetcode"
    print(
        f"The minimum number of operations to turn {word1} into {word2} by only replacing, inserting or removing letters is {solution.minDistance(word1, word2)}"
    )

    word1 = ""
    word2 = "a"
    print(
        f"The minimum number of operations to turn {word1} into {word2} by only replacing, inserting or removing letters is {solution.minDistance(word1, word2)}"
    )

    return None


if __name__ == "__main__":
    main()

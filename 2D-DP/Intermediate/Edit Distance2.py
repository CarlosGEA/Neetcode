"""
Difficulty : Medium
Date created : 28-01-2025
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}

        def dfs(i, j):

            if i == len(word1):
                return len(word2) - j  # just insert

            if j == len(word2):
                return len(word1) - i  # just remove

            if (i, j) in memo:
                return memo[(i, j)]

            res = 0
            if word1[i] == word2[j]:
                res += dfs(i + 1, j + 1)

            else:
                res += 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
                # delete, insert, replace

            memo[(i, j)] = res
            return res

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

"""
Difficulty : Medium
Date created : 29-01-2025
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        memo = {}

        def dfs(i, j):

            if i + j == len(s3):
                return i == len(s1) and j == len(s2)

            if (i, j) in memo:
                return memo[(i, j)]

            res = False
            if i < len(s1) and s1[i] == s3[i + j]:
                res = dfs(i + 1, j)

            if j < len(s2) and s2[j] == s3[i + j]:
                res |= dfs(i, j + 1)

            memo[(i, j)] = res
            return res

        return dfs(0, 0)


def main():

    solution = Solution()

    s1 = "aaaa"
    s2 = "bbbb"
    s3 = "aabbbbaa"
    print(f"Interleaving {s1} and {s2} will give {s3} : {solution.isInterleave(s1, s2, s3)}")

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    print(f"Interleaving {s1} and {s2} will give {s3} : {solution.isInterleave(s1, s2, s3)}")

    s1 = "abc"
    s2 = "xyz"
    s3 = "abxzcy"
    print(f"Interleaving {s1} and {s2} will give {s3} : {solution.isInterleave(s1, s2, s3)}")

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(f"Interleaving {s1} and {s2} will give {s3} : {solution.isInterleave(s1, s2, s3)}")

    return None


if __name__ == "__main__":
    main()

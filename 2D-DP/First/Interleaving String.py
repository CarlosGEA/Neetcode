"""
Difficulty : Medium
Date created : 20-01-2025
"""

from collections import defaultdict


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        icounter = defaultdict(int)
        fcounter = defaultdict(int)

        for s in s1:
            icounter[s] += 1
        for s in s2:
            icounter[s] += 1
        for s in s3:
            fcounter[s] += 1

        if icounter != fcounter:
            return False

        i = j = k = 0

        def dfs(i, j, k):
            if i == len(s1) or j == len(s2) or k == len(s3):
                return True

            res = False

            if s1[i] == s3[k]:
                res |= dfs(i + 1, j, k + 1)

            if s2[j] == s3[k]:
                res |= dfs(i, j + 1, k + 1)

            return res

        return dfs(0, 0, 0)


def main():

    solution = Solution()
    # s1 = "aaaa"
    # s2 = "bbbb"
    # s3 = "aabbbbaa"
    # print(f"Interleaving {s1} and {s2} will give {s3} : {solution.isInterleave(s1, s2, s3)}")

    # s1 = ""
    # s2 = ""
    # s3 = ""
    # print(f"Interleaving {s1} and {s2} will give {s3} : {solution.isInterleave(s1, s2, s3)}")

    # s1 = "abc"
    # s2 = "xyz"
    # s3 = "abxzcy"
    # print(f"Interleaving {s1} and {s2} will give {s3} : {solution.isInterleave(s1, s2, s3)}")

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(f"Interleaving {s1} and {s2} will give {s3} : {solution.isInterleave(s1, s2, s3)}")

    return None


if __name__ == "__main__":
    main()

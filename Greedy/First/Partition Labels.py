"""
Difficulty : Medium
Date created : 08-01-2025
"""

from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        count = defaultdict(int)
        for l in s:
            count[l] += 1

        res = []

        l = r = 0
        cur = set()
        while r < len(s):
            cur.add(s[l])

            while cur:
                cur.add(s[r])
                count[s[r]] -= 1
                if count[s[r]] == 0:
                    del count[s[r]]
                    cur.remove(s[r])
                r += 1

            res.append(r - l)
            l = r

        return res


def main():

    solution = Solution()

    s = "xyxxyzbzbbisl"
    print(
        f"As many substrings as possible with no element appearing in multiple substrings has substring lengths of : {solution.partitionLabels(s)}"
    )

    s = "abcabc"
    print(
        f"As many substrings as possible with no element appearing in multiple substrings has substring lengths of : {solution.partitionLabels(s)}"
    )

    return None


if __name__ == "__main__":
    main()

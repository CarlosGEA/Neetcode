"""
Difficulty : Medium
Date created : 24-01-2025
"""


class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        maxIdx = {}
        for i, l in enumerate(s):
            maxIdx[l] = i

        res = []
        size = 0
        limit = 0
        for i, l in enumerate(s):
            if limit < i:
                res.append(size)
                size = 0
            size += 1
            limit = max(limit, maxIdx[l])

        return res + [size]


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

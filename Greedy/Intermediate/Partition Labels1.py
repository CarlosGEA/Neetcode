"""
Difficulty : Medium
Date created : 11-01-2025
"""


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # slightly smarter method - only store final index of each element
        # use that to find length of substrings and add to it, reset for each susbtring

        charIdx = {}

        for i, c in enumerate(s):
            charIdx[c] = i

        res = []
        lastIdx = 0
        start = 0
        for i, c in enumerate(s):
            lastIdx = max(charIdx[c], lastIdx)

            if i == lastIdx:
                res.append(i - start + 1)
                start = i + 1

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

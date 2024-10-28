"""
Difficulty : Medium
Date created : 27-10-2024
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        chars = {}

        most_common = 0
        left = 0
        for right, c in enumerate(s):
            chars[c] = 1 + chars.get(c, 0)
            most_common = max(most_common, chars[c])

            while (right - left + 1) - most_common > k:
                chars[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res


def main():
    # sliding window, left pointer once not valid

    solution = Solution()

    s = "XYYX"
    k = 2
    print(f"The longest substring is length {solution.characterReplacement(s, k)}")

    s = "AAABABB"
    k = 1
    print(f"The longest substring is length {solution.characterReplacement(s, k)}")

    return None


if __name__ == "__main__":
    main()

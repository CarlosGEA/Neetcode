"""
Difficulty : Medium 
Date created : 31-10-2024
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxc = 0
        l = 0
        chars = {}
        for r, c in enumerate(s):
            chars[c] = chars.get(c, 0) + 1
            maxc = max(maxc, chars[c])

            if (r - l + 1) - maxc > k:
                chars[s[l]] -= 1
                l += 1

        return r - l + 1


def main():

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

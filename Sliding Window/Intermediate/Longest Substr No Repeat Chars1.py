"""
Difficulty : Medium
Date created : 26-10-2024
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        chars = {}
        l = 0
        maxlen = 0
        for r, e in enumerate(s):

            chars[ord(e)] = 1 + chars.get(ord(e), 0)
            if chars[ord(e)] > 1:
                maxlen = max(maxlen, r - l)
                while chars[ord(e)] > 1:
                    chars[ord(s[l])] -= 1
                    l += 1

            maxlen = max(maxlen, r - l + 1)

        return maxlen


def main():

    solution = Solution()

    s = "zxyzxyz"
    print(f"The length of the longest substring is {solution.lengthOfLongestSubstring(s)}")

    s = " "
    print(f"The length of the longest substring is {solution.lengthOfLongestSubstring(s)}")

    s = "xxxx"
    print(f"The length of the longest substring is {solution.lengthOfLongestSubstring(s)}")

    return None


if __name__ == "__main__":
    main()

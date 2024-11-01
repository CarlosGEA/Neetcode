"""
Difficulty : Medium
Date created : 31-10-2024
"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        char_map = defaultdict(int)

        for r, c in enumerate(s):
            char_map[c] += 1

            while char_map[c] > 1:
                char_map[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest


def main():

    solution = Solution()

    s = "zxyzxyz"
    print(f"The length of the longest substring is {solution.lengthOfLongestSubstring(s)}")

    s = " "
    print(f"The length of the longest substring is {solution.lengthOfLongestSubstring(s)}")

    return None


if __name__ == "__main__":
    main()

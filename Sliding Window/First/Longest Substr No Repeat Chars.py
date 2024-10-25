"""
Difficulty : Medium
Date created : 22-10-2024
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # improve by using remove method
        longest = 0

        # l = 0
        # r = 0
        # while r < len(s):
        for l in range(len(s)):
            substr = set(s[l])
            r = l + 1
            while r < len(s) and s[r] not in substr:
                substr.add(s[r])
                r += 1
            longest = max(longest, len(substr))
            # l += 1

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

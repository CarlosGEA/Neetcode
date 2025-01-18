"""
Difficulty : Medium 
Date created : 18-01-2025
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # exxpand outwards

        res = ""
        maxlen = 0

        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxlen:
                    res = s[l : r + 1]
                    maxlen = r - l + 1
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxlen:
                    res = s[l : r + 1]
                    maxlen = r - l + 1
                l -= 1
                r += 1

        return res


def main():

    solution = Solution()

    s = "ababd"
    print(f"The longest palindromic substring is {solution.longestPalindrome(s)}")

    s = "abbc"
    print(f"The longest palindromic substring is {solution.longestPalindrome(s)}")

    return None


if __name__ == "__main__":
    main()

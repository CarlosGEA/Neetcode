"""
Difficulty : 
Date created : 07-12-2024
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # expand outwards from checking
        longest = 0
        res = ""

        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r - l + 1 > longest:
                        longest = r - l + 1
                        res = s[l : r + 1]
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r - l + 1 > longest:
                        longest = r - l + 1
                        res = s[l : r + 1]
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

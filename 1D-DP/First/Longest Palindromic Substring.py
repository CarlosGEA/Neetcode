"""
Difficulty : Medium 
Date created : 03-12-2024
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        length = 0
        longest = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                if j - i + 1 > length and self.isPal(s, i, j):
                    longest = s[i : j + 1]
                    length = j - i + 1

        return longest

    def isPal(self, s, i, j):

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


def main():

    solution = Solution()

    s = "ababd"
    print(f"The longest palindromic substring is {solution.longestPalindrome(s)}")

    s = "abbc"
    print(f"The longest palindromic substring is {solution.longestPalindrome(s)}")

    return None


if __name__ == "__main__":
    main()

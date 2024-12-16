"""
Difficulty : 
Date created : -12-2024
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # can include palindrome check in while part
        res = ""
        maxlen = 0
        for i in range(len(s) - 1):
            start = i
            end = i
            while s[start] == s[end]:
                if end - start + 1 > maxlen:
                    maxlen = end - start + 1
                    res = s[start : end + 1]
                start -= 1
                end += 1

            start = i
            end = i + 1
            while s[start] == s[end]:
                if end - start + 1 > maxlen:
                    maxlen = end - start + 1
                    res = s[start : end + 1]
                start -= 1
                end += 1

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

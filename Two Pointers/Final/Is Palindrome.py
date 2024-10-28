"""
Difficulty : Easy
Date created : 28-10-2024
"""


class Solution:

    def isAlphaNum(self, c: str) -> bool:

        return (
            ord("a") <= ord(c) <= ord("z")
            or ord("A") <= ord(c) <= ord("Z")
            or ord("0") <= ord(c) <= ord("9")
        )

    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:

            while l < r and not self.isAlphaNum(s[l]):
                l += 1

            while r > l and not self.isAlphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():

                return False
            l += 1
            r -= 1

        return True


def main():

    solution = Solution()

    s = "Was it a car or a cat I saw?"
    print(f"The string {s} is a palindrome: {solution.isPalindrome(s)}")

    s = "tab a cat"
    print(f"The string {s} is a palindrome: {solution.isPalindrome(s)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Easy
Date created : 17-10-2024
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Improve by not having an extra string made

        new_s = ""
        for i in s:
            # if i.isalpha():
            #     new_s += i.lower()
            # elif i.isdigit():
            #     new_s += i
            if i.isalnum():
                new_s += i.lower()

        start = 0
        end = len(new_s) - 1
        while start < end:
            if new_s[start] != new_s[end]:
                return False
            start += 1
            end -= 1
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

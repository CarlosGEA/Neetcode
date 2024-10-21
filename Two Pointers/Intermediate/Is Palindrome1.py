"""
Difficulty : Easy
Date created : 20-10-2024
"""

class Solution:

    def isAlphaNum(self, chr):
        return (ord("a") <= ord(chr) <= ord("z") or
               ord("A") <= ord(chr) <= ord("Z") or
               ord("0") <= ord(chr) <= ord("9"))


    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l < r:
            while not self.isAlphaNum(s[l]) and l < r:
                l += 1
            while not self.isAlphaNum(s[r]) and r > l:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

def main():
    solution = Solution()

    s = "Was it a car or a cat I saw?"
    print(f"Is \"{s}\" a palindrome? {solution.isPalindrome(s)}")

    s = "tab a cat"
    print(f"Is \"{s}\" a palindrome? {solution.isPalindrome(s)}")


   
    return None


if __name__ == "__main__":
    main()
"""
Difficulty : Medium
Date created : 04-12-2024
"""


class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPal(s, i, j):
                    count += 1
        return count

    def isPal(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True


def main():

    solution = Solution()

    s = "abc"
    print(f"The number of palindromic substrings in {s} is {solution.countSubstrings(s)}")

    s = "aaa"
    print(f"The number of palindromic substrings in {s} is {solution.countSubstrings(s)}")

    return None


if __name__ == "__main__":
    main()

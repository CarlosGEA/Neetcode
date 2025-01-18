"""
Difficulty : Medium
Date created : 18-01-2025
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res


def main():

    solution = Solution()

    s = "abc"
    print(f"The number of palindromic substrings in {s} is {solution.countSubstrings(s)}")

    s = "aaa"
    print(f"The number of palindromic substrings in {s} is {solution.countSubstrings(s)}")

    return None


if __name__ == "__main__":
    main()

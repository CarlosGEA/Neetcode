"""
Difficulty : Medium
Date created : 07-12-2024
"""


class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0

        for i in range(len(s)):

            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count


def main():

    solution = Solution()

    s = "abc"
    print(f"The number of palindromic substrings in {s} is {solution.countSubstrings(s)}")

    s = "aaa"
    print(f"The number of palindromic substrings in {s} is {solution.countSubstrings(s)}")

    return None


if __name__ == "__main__":
    main()

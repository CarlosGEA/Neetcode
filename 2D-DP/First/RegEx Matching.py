"""
Difficulty : Hard
Date created : 22-01-2025
New attempt : 25-01-2025
New attempt : 
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        '.' Matches any single character
        '*' Matches zero or more of the preceding element.
        """
        return


def main():

    solution = Solution()

    s = "aa"
    p = ".b"
    print(f"The pattern {p} matches expression {s}? : {solution.isMatch(s, p)}")

    s = "nnn"
    p = "n*"
    print(f"The pattern {p} matches expression {s}? : {solution.isMatch(s, p)}")

    s = "xyz"
    p = ".*z"
    print(f"The pattern {p} matches expression {s}? : {solution.isMatch(s, p)}")

    return None


if __name__ == "__main__":
    main()

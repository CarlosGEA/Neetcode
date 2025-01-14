"""
Difficulty : Hard
Date created : 14-01-2025
New attempt : 
"""

from collections import defaultdict
from collections import deque


class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        return


def main():

    solution = Solution()

    words = ["z", "o"]
    print(
        f"In this new language the lexicographic order of letters is {solution.foreignDictionary(words)}"
    )

    words = ["hrn", "hrf", "er", "enn", "rfnn"]
    print(
        f"In this new language the lexicographic order of letters is {solution.foreignDictionary(words)}"
    )

    words = ["abc", "bcd", "cde"]
    print(
        f"In this new language the lexicographic order of letters is {solution.foreignDictionary(words)}"
    )

    words = ["wrtkj", "wrt"]
    print(
        f"In this new language the lexicographic order of letters is {solution.foreignDictionary(words)}"
    )

    return None


if __name__ == "__main__":
    main()

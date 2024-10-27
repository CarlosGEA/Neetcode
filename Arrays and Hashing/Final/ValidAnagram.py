"""
Difficulty : Easy
Date created : 26-10-2024
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = {}
        for idx in range(len(s)):
            count[s[idx]] = count.get(s[idx], 0) + 1
            count[t[idx]] = count.get(t[idx], 0) - 1

        for c in count.values():
            if c != 0:
                return False

        return True


def main():

    solution = Solution()

    s = "racecar"
    t = "carrace"

    print(f"Are {s} and {t} anagrams? : {solution.isAnagram(s, t)}")

    s = "jar"
    t = "jam"
    print(f"Are {s} and {t} anagrams? : {solution.isAnagram(s, t)}")

    return None


if __name__ == "__main__":
    main()

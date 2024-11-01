"""
Difficulty : Medium
Date created : 31-10-2024
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charMap = [0] * 26

        if len(s1) > len(s2):
            return False

        matches = 0
        for i in range(len(s1)):
            charMap[ord(s1[i]) - ord("a")] += 1
            charMap[ord(s2[i]) - ord("a")] -= 1

        for c in charMap:
            if c == 0:
                matches += 1

        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True

            addc = ord(s2[i]) - ord("a")

            charMap[addc] -= 1
            if charMap[addc] == 0:
                matches += 1
            elif charMap[addc] == -1:
                matches -= 1

            remc = ord(s2[i - len(s1)]) - ord("a")
            charMap[remc] += 1
            if charMap[remc] == 0:
                matches += 1
            elif charMap[remc] == 1:
                matches -= 1

        return matches == 26


def main():

    solution = Solution()

    s1 = "abc"
    s2 = "lecabee"
    print(f"s2 contains a substring permutation of s1? {solution.checkInclusion(s1, s2)}")

    s1 = "abc"
    s2 = "lecaabee"
    print(f"s2 contains a substring permutation of s1? {solution.checkInclusion(s1, s2)}")

    s1 = "adc"
    s2 = "dcda"
    print(f"s2 contains a substring permutation of s1? {solution.checkInclusion(s1, s2)}")

    s1 = "abc"
    s2 = "bbbca"
    print(f"s2 contains a substring permutation of s1? {solution.checkInclusion(s1, s2)}")

    return None


if __name__ == "__main__":
    main()

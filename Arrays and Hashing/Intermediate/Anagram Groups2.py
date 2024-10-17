"""
Difficulty : Medium
Date created : 16-10-2024
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Use chars over sorting
        res = defaultdict(list)

        for s in strs:
            letters = [0] * 26
            for c in s:
                letters[ord(c) - ord("a")] += 1
            res[tuple(letters)].append(s)
        return res.values()


def main():

    solution = Solution()

    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    print(f"The group of anagrams are {solution.groupAnagrams(strs)}")

    strs = ["x"]
    print(f"The group of anagrams are {solution.groupAnagrams(strs)}")

    strs = [""]
    print(f"The group of anagrams are {solution.groupAnagrams(strs)}")

    return None


if __name__ == "__main__":
    main()

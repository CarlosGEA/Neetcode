"""
Difficulty : Medium
Date created : 26-10-2024
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        groups = {}

        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord("a")] += 1

            if tuple(chars) not in groups:
                groups[tuple(chars)] = [s]

            else:
                groups[tuple(chars)].append(s)

        return groups.values()


def main():

    solution = Solution()

    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    print(f"The anagram groups are : {solution.groupAnagrams(strs)}")

    strs = ["x"]
    print(f"The anagram groups are : {solution.groupAnagrams(strs)}")

    strs = ["stop", "pots", "reed", "", "tops", "deer", "opts", ""]
    print(f"The anagram groups are : {solution.groupAnagrams(strs)}")

    return None


if __name__ == "__main__":
    main()

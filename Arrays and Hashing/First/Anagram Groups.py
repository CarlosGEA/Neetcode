"""
Difficulty : Medium
Date created : 10-10-2024
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sublists = []
        anagrams = {}
        for string in strs:
            sorted_string = sorted(string)
            # if sorted_string in anagrams.values():
            if tuple(sorted_string) in anagrams.keys():
                # sublists[
                #     list(anagrams.keys())[list(anagrams.values()).index(sorted_string)]
                # ].append(string)
                sublists[anagrams[tuple(sorted_string)]].append(string)
            else:
                # anagrams[len(sublists)] = sorted_string
                anagrams[tuple(sorted_string)] = len(sublists)
                sublists.append([string])
        return sublists


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

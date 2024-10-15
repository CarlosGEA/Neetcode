"""
Difficulty : Medium
Date created : 14-10-2024
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        anagrams = defaultdict(list)
        # sublists = []
        count = 0
        for s in strs:
            # sorted_s = tuple(sorted(s))
            sorted_s = "".join(sorted(s))
            anagrams[sorted_s].append(s)
            # if sorted_s in anagrams:
            #     sublists[anagrams[sorted_s]].append(s)
            # else:
            #     anagrams[sorted_s] = count
            #     sublists.append([s])
            #     count += 1
        return anagrams.values() #sublists
    



def main():

    solution = Solution()

    strs = ["act","pots","tops","cat","stop","hat"]
    print(f"The group of anagrams are {solution.groupAnagrams(strs)}")

    strs = ["x"]
    print(f"The group of anagrams are {solution.groupAnagrams(strs)}")

    strs = [""]
    print(f"The group of anagrams are {solution.groupAnagrams(strs)}")


    
    return None


if __name__ == "__main__":
    main()
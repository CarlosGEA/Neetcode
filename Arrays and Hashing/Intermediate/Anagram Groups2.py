"""
Difficulty : Medium
Date created : 14-10-2024
"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Use chars over sorting
        
        return



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
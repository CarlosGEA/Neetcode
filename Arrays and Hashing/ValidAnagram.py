"""
Difficulty : Easy
Date created : 10-10-2024
Status - Optimal
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = ''.join(sorted(s))
        # t = ''.join(sorted(t))
        return sorted(s) == sorted(t)
        


def main():

    solution = Solution()

    s= "racecar"
    t = "carrace"

    print(f"Are {s} and {t} anagrams? : {solution.isAnagram(s, t)}")

    s = "jar"
    t = "jam"
    print(f"Are {s} and {t} anagrams? : {solution.isAnagram(s, t)}")
   
    return None


if __name__ == "__main__":
    main()
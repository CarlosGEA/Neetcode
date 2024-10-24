"""
Difficulty : Hard
Date created : 24-10-2024
"""
# Complexity -- Time: O(n  * m), Space: O(m)
# n - len(s), m - len(t)
class Solution:

    def isValid(self, s: dict[str], t: dict[str]) -> bool:
        for k, v in t.items():
            if k not in s or v > s[k]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:

        res = ""

        if len(t) > len(s):
            return res

        if len(t) == len(s):
            chars = {}
            for i in range(len(s)):
                chars[t[i]] = chars.get(t[i], 0) + 1 
                chars[s[i]] = chars.get(s[i], 0) - 1 

            for count in chars.values():
                if count != 0:
                    return res
            return s
        
        compare = {}
        for i in t:
            compare[i] = 1 + compare.get(i, 0)
        
        left = 0
        check = {}
        for right, letter in enumerate(s):
            check[letter] = 1 + check.get(letter, 0)
            while self.isValid(check, compare):
                substr = s[left: right + 1]
                if len(res) == 0 or len(substr) < len(res):
                    res = substr
                check[s[left]] -= 1
                left += 1
        return res


def main():

    solution = Solution()

    s = "OUZODYXAZV"
    t = "XYZ"
    print(f"The smallest substring of s containing all elements of t is {solution.minWindow(s, t)}")

    s = "xyz"
    t = "xyz"
    print(f"The smallest substring of s containing all elements of t is {solution.minWindow(s, t)}")

    s = "x"
    t = "xy"
    print(f"The smallest substring of s containing all elements of t is {solution.minWindow(s, t)}")
  
    return None


if __name__ == "__main__":
    main()
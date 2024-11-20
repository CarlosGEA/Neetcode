"""
Difficulty : Medium
Date created : 20-11-2024
"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def backtrack(l, cur):

            if l == len(s):
                res.append(cur.copy())
                return

            for r in range(l, len(s)):
                if self.isPal(s, l, r):
                    cur.append(s[l : r + 1])
                    backtrack(r + 1, cur)
                    cur.pop()

        backtrack(0, [])

        return res

    def isPal(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


def main():

    solution = Solution()

    s = "aab"
    print(f"The palindromes are : {solution.partition(s)}")

    s = "a"
    print(f"The palindromes are : {solution.partition(s)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 10-11-2024
New attempt : 14-11-2024
New attempt : 
"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        # have palindrome check of string
        # check left and right of current palindrome ends plus have a running part

        return


def main():

    solution = Solution()

    s = "aab"
    print(f"The possible palindromes of {s} are {solution.partition(s)}")

    s = "a"
    print(f"The possible palindromes of {s} are {solution.partition(s)}")

    s = "cdd"
    print(f"The possible palindromes of {s} are {solution.partition(s)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 21-10-2024
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        res = []
        bracket = []

        def iterateN(open, close):

            if close == n:
                res.append("".join(bracket))
                return

            if open < n:
                bracket.append("(")
                iterateN(open + 1, close)
                bracket.pop()

            if open - close > 0:
                bracket.append(")")
                iterateN(open, close + 1)
                bracket.pop()

        iterateN(0, 0)

        return res


def main():

    solution = Solution()

    n = 1
    print(f"For n={n}, the possible valid solutions are {solution.generateParenthesis(n)}")

    n = 3
    print(f"For n={n}, the possible valid solutions are {solution.generateParenthesis(n)}")
    return None


if __name__ == "__main__":
    main()

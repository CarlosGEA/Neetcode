"""
Difficulty : Medium
Date created : 18-10-2024
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        res = []
        bracket = []

        def recur(open, close):
            if open < n:
                bracket.append("(")
                recur(open + 1, close)
                bracket.pop()

            if open > close:
                bracket.append(")")
                recur(open, close + 1)
                bracket.pop()
            else:
                res.append("".join(bracket))
                return

        recur(0, 0)
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

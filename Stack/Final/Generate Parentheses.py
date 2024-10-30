"""
Difficulty : Medium
Date created : 30-10-2024
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        res = []
        stack = []

        def recur(openP, closeP):

            if n == openP == closeP:
                res.append("".join(stack))
                return

            if n > openP:
                stack.append("(")
                recur(openP + 1, closeP)
                stack.pop()

            if openP > closeP:
                stack.append(")")
                recur(openP, closeP + 1)
                stack.pop()

        recur(0, 0)
        return res


def main():

    solution = Solution()

    n = 5
    ans = solution.generateParenthesis(n)
    print(f"From {n} brackets we can make {ans}")

    return None


if __name__ == "__main__":
    main()

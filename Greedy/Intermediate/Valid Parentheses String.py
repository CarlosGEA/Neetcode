"""
Difficulty : Medium
Date created : 12-01-2025
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        # do greedy solution
        # min and max

        minB = maxB = 0

        for c in s:
            if c == "(":
                minB += 1
                maxB += 1
            elif c == ")":
                minB -= 1
                maxB -= 1
            else:
                minB -= 1
                maxB += 1

            if maxB < 0:
                return False

            minB = max(minB, 0)

        return minB == 0


def main():

    solution = Solution()

    s = "((**)"
    print(f"This set of parentheses is valid {solution.checkValidString(s)}")

    s = "(((*)"
    print(f"This set of parentheses is valid {solution.checkValidString(s)}")

    s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
    print(f"This set of parentheses is valid {solution.checkValidString(s)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 09-01-2025
"""


class Solution:
    def checkValidString(self, s: str) -> bool:

        openB = wild = 0
        cur = []
        for c in s:
            if c == "(":
                openB += 1
                cur.append(c)

            elif c == "*":
                wild += 1
                cur.append(c)

            elif openB:
                openB -= 1

                dummy = 0
                while cur[-1] == "*":
                    cur.pop()
                    dummy += 1

                cur.pop()
                while dummy:
                    cur.append("*")
                    dummy -= 1

            elif wild:
                wild -= 1
                cur.pop()

            else:
                return False

        while openB and cur[-1] != "(":
            cur.pop()
            openB -= 1

        return openB == 0


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

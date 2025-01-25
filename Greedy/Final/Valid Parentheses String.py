"""
Difficulty : Medium
Date created : 24-01-2025
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        # good

        maxOpen = minOpen = 0

        for b in s:
            if b == "(":
                maxOpen += 1
                minOpen += 1

            elif b == ")":
                maxOpen -= 1
                minOpen -= 1

            else:
                maxOpen += 1
                minOpen -= 1

            if maxOpen < 0:
                return False

            minOpen = max(0, minOpen)

        return minOpen == 0


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

"""
Difficulty : Medium
Date created : 30-10-2024
"""


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for t in tokens:

            if len(t) == 1 and not t.isdigit():
                match t:
                    case "+":
                        stack.append(stack.pop() + stack.pop())
                    case "*":
                        stack.append(stack.pop() * stack.pop())
                    case "-":
                        second = stack.pop()
                        stack.append(stack.pop() - second)
                    case "/":
                        second = stack.pop()
                        stack.append(int(stack.pop() / second))
                continue

            stack.append(int(t))

        return stack[0]


def main():

    solution = Solution()

    tokens = [
        "10",
        "6",
        "9",
        "3",
        "+",
        "-11",
        "*",
        "/",
        "*",
        "17",
        "+",
        "5",
        "+",
    ]  # ["1","2","+","3","*","4","-"]
    print(f"The reverse polish calculation of the inputs is : {solution.evalRPN(tokens)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Easy
Date created : 30-10-2024
"""


class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {"}": "{", "]": "[", ")": "("}
        stack = []

        for b in s:
            if stack and pairs.get(b, None) == stack[-1]:
                stack.pop()
            else:
                stack.append(b)

        return len(stack) == 0


def main():

    solution = Solution()

    s = "[]"
    print(f"String {s} has valid parentheses? : {solution.isValid(s)}")

    s = "([{}])"
    print(f"String {s} has valid parentheses? : {solution.isValid(s)}")

    s = "[(])"
    print(f"String {s} has valid parentheses? : {solution.isValid(s)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Easy
Date created : 14-10-2024
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if stack and 3 > ord(i) - ord(stack[-1])  > 0:
                stack.pop()
            else:
                stack.append(i)
        return not stack # If empty returns False, i.e. it's valid


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

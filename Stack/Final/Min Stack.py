"""
Difficulty : Medium
Date created : 30-10-2024
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
            return None
        self.minStack.append(min(self.minStack[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


def main():
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(0)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())

    return None


if __name__ == "__main__":
    main()

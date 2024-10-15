"""
Difficulty : Medium
Date created : 15-10-2024
"""


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        nums = []
        for i in tokens:
            if i.isdigit() or (len(i) > 1 and i[0] =="-"):
                nums.append(int(i))
            elif i == "+":
                nums.append(nums.pop() + nums.pop())
            elif i == "-":
                first = nums.pop()
                nums.append(nums.pop() - first)
            elif i == "*":
                nums.append(nums.pop() * nums.pop())
            elif i == "/":
                first = nums.pop()
                nums.append(int(nums.pop() / first))
        return nums[0]


def main():

    solution = Solution()

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]#["1","2","+","3","*","4","-"]
    print(f"The reverse polish calculation of the inputs is : {solution.evalRPN(tokens)}")


    return None


if __name__ == "__main__":
    main()

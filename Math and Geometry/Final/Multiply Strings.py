"""
Difficulty : Medium
Date created : 27-01-2025
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        res = 0
        for i, n1 in enumerate(num1[::-1]):
            cur = 0
            for j, n2 in enumerate(num2[::-1]):
                cur += (10**j) * (ord(n1) - ord("0")) * (ord(n2) - ord("0"))

            res += (10**i) * cur

        return str(res)


def main():

    solution = Solution()

    num1 = "3"
    num2 = "4"

    print(f"The product of {num1} and {num2} is {solution.multiply(num1, num2)}")

    num1 = "111"
    num2 = "222"
    print(f"The product of {num1} and {num2} is {solution.multiply(num1, num2)}")

    return None


if __name__ == "__main__":
    main()

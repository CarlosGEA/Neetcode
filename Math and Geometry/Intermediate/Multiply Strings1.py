"""
Difficulty : Medium
Date created : 13-01-2025
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        for i, digit1 in enumerate(num1[::-1]):
            temp = 0
            for j, digit2 in enumerate(num2[::-1]):
                temp += (10**j) * int(digit1) * int(digit2)
            res += (10**i) * temp

        return str(res)


def main():

    return None


if __name__ == "__main__":
    main()

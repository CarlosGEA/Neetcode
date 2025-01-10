"""
Difficulty : Medium
Date created : 09-01-2025
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        for i, n1 in enumerate(num1[::-1]):
            cur = 0
            for j, n2 in enumerate(num2[::-1]):
                cur += (10**j) * int(n1) * int(n2)

            res += (10**i) * cur

        return str(res)


def main():

    return None


if __name__ == "__main__":
    main()

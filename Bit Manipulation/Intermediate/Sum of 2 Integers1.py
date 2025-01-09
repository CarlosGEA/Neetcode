"""
Difficulty : Medium
Date created : 21-12-2024
New attempt : 06-01-2025
New attempt : 09-01-2025
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:

        maxI = 0x7FFFFFFF
        mask = 0xFFFFFFFF

        while b:
            carry = (a & b) << 1 & mask
            a = (a ^ b) & mask
            b = carry

        return a if a < maxI else ~(a ^ mask)


def main():

    solution = Solution()
    a = 1
    b = 1
    print(f"The sum of {a} and {b} is {solution.getSum(a,b)}")

    a = 4
    b = 7
    print(f"The sum of {a} and {b} is {solution.getSum(a,b)}")

    return None


if __name__ == "__main__":
    main()

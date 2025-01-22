"""
Difficulty : Medium
Date created : 19-01-2025
New attempt : 22-01-2025
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        maxInt = 0x7FFFFFFF

        while b:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry 

        return a if a < maxInt else ~(a^mask)


def main():

    solution = Solution()
    a = -1
    b = 1
    print(f"The sum of {a} and {b} is {solution.getSum(a,b)}")

    a = 4 # 100
    b = 7 # 111
    print(f"The sum of {a} and {b} is {solution.getSum(a,b)}")

    return None


if __name__ == "__main__":
    main()

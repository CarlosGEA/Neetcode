"""
Difficulty : Easy
Date created : 17-12-2024
"""


class Solution:
    def hammingWeight(self, n: int) -> int:

        str_n = str(bin(n))
        res = 0
        for i in str_n:
            if i == "1":
                res += 1

        return res


def main():

    solution = Solution()

    n = 0b00000000000000000000000000010111
    print(f"The number of 1's in n is {solution.hammingWeight(n)}")

    n = 0b01111111111111111111111111111101
    print(f"The number of 1's in n is {solution.hammingWeight(n)}")

    return None


if __name__ == "__main__":
    main()

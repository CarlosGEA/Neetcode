"""
Difficulty : Easy
Date created : 19-01-2025
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        # can be more optimal
        res = 0
        for i in range(32):
            if (n >> i) & 1:
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

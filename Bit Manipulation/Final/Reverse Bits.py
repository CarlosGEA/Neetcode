"""
Difficulty : Easy
Date created : 19-01-2025
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            dig = (n >> i) & 1
            res += dig << (31 - i)

        return res


def main():

    solution = Solution()

    n = 0b00000000000000000000000000010101
    print(f"The bit reversed number of {int(n)} is {solution.reverseBits(n)} ")

    return None


if __name__ == "__main__":
    main()

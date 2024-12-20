"""
Difficulty : Easy
Date created : 20-12-2024
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count


def main():

    solution = Solution()

    n = 0b00000000000000000000000000010111
    print(f"The number of 1's in n is {solution.hammingWeight(n)}")

    n = 0b01111111111111111111111111111101
    print(f"The number of 1's in n is {solution.hammingWeight(n)}")

    return None


if __name__ == "__main__":
    main()

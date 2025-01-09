"""
Difficulty : Medium
Date created : 06-01-2025
New attempt : 09-01-2025
"""

import math


class Solution:
    def reverse(self, x: int) -> int:

        minI = -2 ** 31
        maxI = (2 ** 31) - 1

        res = 0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            res = (res * 10) + digit

        return res if minI <= res <= maxI else 0


def main():

    solution = Solution()

    x = 1234
    print(f"The reverse of {x} within the signed 32-bit integer range is {solution.reverse(x)} ")

    x = -1234
    print(f"The reverse of {x} within the signed 32-bit integer range is {solution.reverse(x)} ")

    x = 1234236467
    print(f"The reverse of {x} within the signed 32-bit integer range is {solution.reverse(x)} ")

    return None


if __name__ == "__main__":
    main()

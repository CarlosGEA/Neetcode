"""
Difficulty : Medium
Date created : 19-01-2025
"""

import math

class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        minI = -0x80000000
        maxI = 0x7FFFFFFF

        while x:

            if res > maxI or res < minI:
                return 0

            val = int(math.fmod(x, 10))
            res = (res * 10) + val
            

            x = int(x/10)

        return 0 if res > maxI or res < minI else res


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

"""
Difficulty : Medium
Date created : 18-12-2024
"""


class Solution:
    def reverse(self, x: int) -> int:
        MIN = - (2 ** 31)
        MAX = (2 ** 31) - 1

        neg = False
        x_str = str(x)
        if x < 0:
            neg = True
            x_str = x_str[1:]

        x = int(x_str[::-1]) 
        x *= -1 if neg else 1
        
        if x < MIN or x > MAX:
            return 0

        return x


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

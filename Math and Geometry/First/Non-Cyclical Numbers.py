"""
Difficulty : Easy
Date created : 08-01-2025
"""


class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while n not in seen:
            seen.add(n)
            if n == 1:
                return True

            next_n = 0

            while n:
                next_n += (n % 10) ** 2
                n //= 10

            n = next_n

        return False


def main():

    solution = Solution()

    n = 101
    print(f"Is {n} a cyclical number ? : {solution.isHappy(n)}")

    n = 7
    print(f"Is {n} a cyclical number ? : {solution.isHappy(n)}")

    return None


if __name__ == "__main__":
    main()

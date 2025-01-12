"""
Difficulty : Easy
Date created : 12-01-2025
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            new_n = 0
            while n:
                new_n += (n % 10) ** 2
                n //= 10

            n = new_n

        return True


def main():

    solution = Solution()

    n = 101
    print(f"Is {n} a cyclical number ? : {solution.isHappy(n)}")

    n = 7
    print(f"Is {n} a cyclical number ? : {solution.isHappy(n)}")

    return None


if __name__ == "__main__":
    main()

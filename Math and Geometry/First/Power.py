"""
Difficulty : Medium
Date created : 11-01-2025
New attempt : 14-01-2025
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x

            val = helper(x * x, n // 2)
            return val * x if n % 2 != 0 else val

        res = helper(x, abs(n))
        return res if n > 0 else 1 / res


def main():

    solution = Solution()

    x = 2.00000
    n = 5
    print(f"{x} ^ {n} = {solution.myPow(x, n)}")

    x = 1.10000
    n = 10
    print(f"{x} ^ {n} = {solution.myPow(x, n)}")

    x = 2.00000
    n = -3
    print(f"{x} ^ {n} = {solution.myPow(x, n)}")

    return None


if __name__ == "__main__":
    main()

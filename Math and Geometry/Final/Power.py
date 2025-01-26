"""
Difficulty : Medium
Date created : 26-01-2025
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # helper

        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            ans = helper(x * x, n // 2)

            return ans if n % 2 == 0 else ans * x

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

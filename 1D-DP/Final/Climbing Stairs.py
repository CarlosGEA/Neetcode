"""
Difficulty : Easy
Date created : 18-01-2025
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        frst = scnd = 1

        for _ in range(n - 1):
            tmp = scnd
            scnd += frst
            frst = tmp

        return scnd


def main():

    solution = Solution()

    n = 2
    print(f"Number of ways to do {n} steps with step sizes of {{1,2}} is {solution.climbStairs(n)}")

    n = 8
    print(f"Number of ways to do {n} steps with step sizes of {{1,2}} is {solution.climbStairs(n)}")

    return None


if __name__ == "__main__":
    main()

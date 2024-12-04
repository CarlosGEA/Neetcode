"""
Difficulty : Easy
Date created : 03-12-2024
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        first = 0
        second = 1

        for _ in range(n):
            temp = second
            second += first
            first = temp

        return second


def main():

    solution = Solution()

    n = 2
    print(f"Number of ways to do {n} steps with step sizes of {{1,2}} is {solution.climbStairs(n)}")

    n = 8
    print(f"Number of ways to do {n} steps with step sizes of {{1,2}} is {solution.climbStairs(n)}")

    return None


if __name__ == "__main__":
    main()

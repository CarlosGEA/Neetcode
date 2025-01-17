"""
Difficulty : Easy
Date created : 18-01-2025
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        pos = [None] * (n + 1)

        pos[0] = 1
        pos[1] = 1

        for i in range(2, n + 1):
            pos[i] = pos[i - 1] + pos[i - 2]

        return pos[-1]


def main():

    solution = Solution()

    n = 2
    print(f"Number of ways to do {n} steps with step sizes of {{1,2}} is {solution.climbStairs(n)}")

    n = 8
    print(f"Number of ways to do {n} steps with step sizes of {{1,2}} is {solution.climbStairs(n)}")

    return None


if __name__ == "__main__":
    main()

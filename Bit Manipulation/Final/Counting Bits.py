"""
Difficulty : Easy
Date created : 19-01-2025
"""


class Solution:
    def countBits(self, n: int) -> list[int]:

        if n == 0:
            return [0]

        res = [0] * (n + 1)
        res[1] = 1
        cur = 1
        for i in range(2, n):
            if i % cur == 0:
                cur *= 2
            res[i] = 1 + res[i - cur]

        return res


def main():

    solution = Solution()

    n = 4
    print(f"The number of 1 bits in every digit up to {n} is {solution.countBits(n)}")

    return None


if __name__ == "__main__":
    main()

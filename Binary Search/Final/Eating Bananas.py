"""
Difficulty : Medium
Date created : 03-11-2024
"""


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        l = 1
        r = max(piles)
        res = float("inf")

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += p // k
                hours += 1 if p % k else 0

            if hours > h:
                l = k + 1

            elif hours <= h:
                r = k - 1
                res = min(res, k)

        return res


def main():
    solution = Solution()

    piles = [1, 4, 3, 2]
    h = 9
    print(
        f"The smallest eating rate that takes less than {h} hours is {solution.minEatingSpeed(piles, h)}"
    )

    piles = [25, 10, 23, 4]
    h = 4
    print(
        f"The smallest eating rate that takes less than {h} hours is {solution.minEatingSpeed(piles, h)}"
    )

    return


if __name__ == "__main__":
    main()

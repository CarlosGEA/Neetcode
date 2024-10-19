"""
Difficulty : Medium
Date created : 19-10-2024
"""


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        low = 1
        high = max(piles)
        min_k = high

        while low <= high:
            mid = (low + high) // 2
            count = 0
            for food in piles:
                count += (food // mid) + min(1, food % mid) # (1 if food % mid > 0 else 0) or -(-food // mid)
            if count > h:
                low = mid + 1
            else:
                high = mid - 1
                min_k = mid
        return min_k


def main():
    solution = Solution()

    piles = [1, 4, 3, 2]
    h = 9
    print(f"The smallest eating rate that takes less than {h} hours is {solution.minEatingSpeed(piles, h)}")

    piles = [25, 10, 23, 4]
    h = 4
    print(f"The smallest eating rate that takes less than {h} hours is {solution.minEatingSpeed(piles, h)}")


    return


if __name__ == "__main__":
    main()

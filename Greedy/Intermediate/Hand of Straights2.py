"""
Difficulty : Medium
Date created : 14-01-2025
"""

from collections import defaultdict


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # instead of sorting, use while to get down to smallest possible start and go from there up to
        # current num being checked, within traversing through groups and if not possible returning false

        if len(hand) % groupSize != 0:
            return False

        count = defaultdict(int)
        for num in hand:
            count[num] += 1

        for num in hand:

            if not count[num]:
                continue

            start = num
            while count[start - 1]:
                start -= 1

            while start <= num:
                for i in range(start, start + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
                start += groupSize

        return True


def main():

    solution = Solution()

    hand = [1, 2, 4, 2, 3, 5, 3, 4]
    groupSize = 4
    print(
        f"Can straight hands of size {groupSize} be made? {solution.isNStraightHand(hand, groupSize)}"
    )

    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3
    print(
        f"Can straight hands of size {groupSize} be made? {solution.isNStraightHand(hand, groupSize)}"
    )

    return None


if __name__ == "__main__":
    main()

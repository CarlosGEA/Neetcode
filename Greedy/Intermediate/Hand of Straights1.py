"""
Difficulty : Medium
Date created : 11-01-2025
"""

from collections import defaultdict


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # use hash map for count and sort
        if len(hand) % groupSize != 0:
            return False

        count = defaultdict(int)

        for num in hand:
            count[num] += 1

        for num in sorted(hand):
            if count[num] == 0:
                continue
            for val in range(num, num + groupSize):
                if val in count and count[val] != 0:
                    count[val] -= 1

                else:
                    return False

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

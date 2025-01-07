"""
Difficulty : Medium
Date created : 07-01-2025
"""


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        groups = [[] for _ in range((len(hand) // groupSize))]
        for num in hand:
            for group in groups:
                if len(group) == groupSize or num in group or (group and group[0] + groupSize - 1 < num):
                    continue
                else:
                    group.append(num)
                    break

        return all(len(group) == groupSize for group in groups)


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

"""
Difficulty : Medium
Date created : 08-01-2025
New attempt : 12-01-2025
"""


class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        # if greater don't update else try and update
        # return if same as target
        res = triplets[0]
        for triplet in triplets:
            a, b, c = triplet

            if a > target[0] or b > target[1] or c > target[2]:
                continue

            res = [max(res[0], a), max(res[1], b), max(res[2], c)]

            if res == target:
                return True

        return False


def main():

    solution = Solution()

    triplets = [[1, 2, 3], [7, 1, 1]]
    target = [7, 2, 3]
    print(
        f"The target can be formed by the given method : {solution.mergeTriplets(triplets, target)}"
    )

    triplets = [[2, 5, 6], [1, 4, 4], [5, 7, 5]]
    target = [5, 4, 6]
    print(
        f"The target can be formed by the given method : {solution.mergeTriplets(triplets, target)}"
    )

    return None


if __name__ == "__main__":
    main()

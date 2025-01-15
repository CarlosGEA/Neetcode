"""
Difficulty : Medium
Date created : 15-01-2025
"""


class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:

        res = [0, 0, 0]

        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            res = [max(res[0], a), max(res[1], b), max(res[2], c)]

        return res == target


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

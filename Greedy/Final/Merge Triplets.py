"""
Difficulty : Medium
Date created : 24-01-2025
"""


class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:

        x = y = z = 0
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            x = max(a, x)
            y = max(b, y)
            z = max(c, z)

        return [x, y, z] == target


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

"""
Difficulty : Medium
Date created : 14-01-2025
"""

from collections import defaultdict


class CountSquares:
    # overcomplicated it -> just look for diagonals
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: list[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        x1 = point[0]
        y1 = point[1]
        res = 0
        for point2 in self.points.keys():
            if tuple(point) == point2:
                continue

            x2 = point2[0]
            y2 = point2[1]

            if x1 != x2 and y1 != y2 and (x1, y2) in self.points and (x2, y1) in self.points:
                res += self.points[point2] * self.points[(x1, y2)] * self.points[(x2, y1)]

        return res


def main():

    countSquares = CountSquares()
    countSquares.add([1, 1])
    countSquares.add([2, 2])
    countSquares.add([1, 2])
    print(countSquares.count([2, 1]))  # return 1.
    print(countSquares.count([3, 3]))  # return 0.
    countSquares.add([2, 2])  # Duplicate points are allowed.
    print(countSquares.count([2, 1]))  # return 2.

    print("\nNew square count\n")

    countSquares = CountSquares()
    countSquares.add([3, 3])
    countSquares.add([6, 3])
    countSquares.add([3, 6])
    print(countSquares.count([6, 6]))  # return 1.
    countSquares.add([2, 2])
    countSquares.add([6, 2])
    countSquares.add([2, 6])
    print(countSquares.count([6, 6]))  # return 2.
    countSquares.add([2, 2])
    countSquares.add([3, 3])
    print(countSquares.count([6, 6]))  # return 4.
    countSquares.add([6, 3])
    countSquares.add([3, 6])
    print(countSquares.count([6, 6]))  # return 10

    return None


if __name__ == "__main__":
    main()

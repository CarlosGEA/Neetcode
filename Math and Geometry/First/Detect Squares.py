"""
Difficulty : Medium
Date created : 11-01-2025
"""

from collections import defaultdict


class CountSquares:

    def __init__(self):
        self.points = set()
        self.pointsCount = defaultdict(int)
        self.pointsX = defaultdict(set)
        self.pointsY = defaultdict(set)

    def add(self, point: list[int]) -> None:
        self.points.add(tuple(point))
        self.pointsCount[tuple(point)] += 1
        self.pointsX[point[0]].add(point[1])
        self.pointsY[point[1]].add(point[0])

        return None

    def count(self, point: list[int]) -> int:
        seen = set()
        count = 0
        for existing in self.points:
            # same
            if existing == tuple(point):
                continue

            # y-parallel
            elif existing[0] == point[0]:
                # [2,1] and [2,2] -> check [?,1] and [?,2]
                intersection = self.pointsY[existing[1]] and self.pointsY[point[1]]
                if intersection:
                    for num in intersection:
                        corner1 = (num, existing[1])
                        corner2 = (num, point[1])
                        if (
                            corner1 == tuple(point)
                            or corner2 == tuple(point)
                            or corner1 in seen
                            or corner2 in seen
                        ):
                            continue
                        elif corner1 in self.points and corner2 in self.points:
                            seen.add(tuple(existing))
                            count += (
                                self.pointsCount[existing]
                                * self.pointsCount[corner1]
                                * self.pointsCount[corner2]
                            )

            # x-parallel
            elif existing[1] == point[1]:
                intersection = self.pointsX[existing[0]] and self.pointsX[point[0]]
                if intersection:
                    for num in intersection:
                        corner1 = (existing[0], num)
                        corner2 = (point[0], num)
                        if (
                            corner1 == tuple(point)
                            or corner2 == tuple(point)
                            or corner1 in seen
                            or corner2 in seen
                        ):
                            continue
                        elif corner1 in self.points and corner2 in self.points:
                            seen.add(tuple(existing))
                            count += (
                                self.pointsCount[existing]
                                * self.pointsCount[corner1]
                                * self.pointsCount[corner2]
                            )

            # diagonal
            else:
                corner1 = (existing[0], point[1])
                corner2 = (point[0], existing[1])
                if (
                    corner1 == tuple(point)
                    or corner2 == tuple(point)
                    or corner1 in seen
                    or corner2 in seen
                ):
                    continue

                elif corner1 in self.points and corner2 in self.points:
                    seen.add(tuple(existing))
                    count += (
                        self.pointsCount[existing]
                        * self.pointsCount[corner1]
                        * self.pointsCount[corner2]
                    )
        return count


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

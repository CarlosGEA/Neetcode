"""
Difficulty : Medium
Date created : 20-11-2024
"""

import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # can do max heap to store less values in heap

        maxHeap = []
        heapq.heapify(maxHeap)

        for x, y in points:
            dist_sq = - (x ** 2 + y ** 2)
            heapq.heappush(maxHeap, (dist_sq, [x, y]))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [p[1] for p in maxHeap]


def main():

    solution = Solution()

    points = [[0, 2], [2, 2]]
    k = 1
    print(f"The {k}th closest points to origin is {solution.kClosest(points, k)}")

    points = [[0, 2], [2, 0], [2, 2]]
    k = 2
    print(f"The {k}th closest points to origin is {solution.kClosest(points, k)}")

    return None


if __name__ == "__main__":
    main()

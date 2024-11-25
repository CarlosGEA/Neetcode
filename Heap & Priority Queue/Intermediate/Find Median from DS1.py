"""
Difficulty : Hard
Date created : 25-11-2024
"""

import heapq


class MedianFinder:
    def __init__(self):

        self.minS = []  # stores all numbers above median
        self.maxS = []  # stores all numbers below median

        heapq.heapify(self.minS)
        heapq.heapify(self.maxS)

    def addNum(self, num: int) -> None:

        if self.minS and num > self.minS[0]:
            heapq.heappush(self.minS, num)

        else:
            heapq.heappush(self.maxS, -num)

        if len(self.minS) - len(self.maxS) > 1:
            heapq.heappush(self.maxS, -heapq.heappop(self.minS))

        if len(self.maxS) - len(self.minS) > 1:
            heapq.heappush(self.minS, -heapq.heappop(self.maxS))

    def findMedian(self) -> float:

        if len(self.minS) > len(self.maxS):
            return self.minS[0]

        elif len(self.minS) < len(self.maxS):
            return -self.maxS[0]

        return (self.minS[0] - self.maxS[0]) / 2


def main():

    medianFinder = MedianFinder()
    medianFinder.addNum(1)  # arr = [1]
    print(medianFinder.findMedian())  # return 1.0
    medianFinder.addNum(3)  # arr = [1, 3]
    print(medianFinder.findMedian())  # return 2.0
    medianFinder.addNum(2)  # arr[1, 2, 3]
    print(medianFinder.findMedian())  # return 2.0

    return None


if __name__ == "__main__":
    main()

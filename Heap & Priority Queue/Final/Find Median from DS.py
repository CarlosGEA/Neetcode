"""
Difficulty : Hard
Date created : 04-12-2024
"""

import heapq


class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:

        if self.minHeap and num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)

        else:
            heapq.heappush(self.maxHeap, -num)

        if len(self.minHeap) - len(self.maxHeap) > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

        if len(self.maxHeap) - len(self.minHeap) > 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:

        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]

        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]

        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2


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

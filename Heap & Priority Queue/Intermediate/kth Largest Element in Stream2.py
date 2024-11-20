"""
Difficulty : Easy
Date created : 20-11-2024
"""

import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.maxHeap = nums

        heapq.heapify(self.maxHeap)

        while len(self.maxHeap) > self.k:
            heapq.heappop(self.maxHeap)

    def add(self, val: int) -> int:

        heapq.heappush(self.maxHeap, val)
        if len(self.maxHeap) > self.k:
            heapq.heappop(self.maxHeap)

        return self.maxHeap[0]


def main():
    kthLargest = KthLargest(3, [1, 2, 3, 3])
    print(kthLargest.add(3))  # return 3
    print(kthLargest.add(5))  # return 3
    print(kthLargest.add(6))  # return 3
    print(kthLargest.add(7))  # return 5
    print(kthLargest.add(8))  # return 6

    return None


if __name__ == "__main__":
    main()

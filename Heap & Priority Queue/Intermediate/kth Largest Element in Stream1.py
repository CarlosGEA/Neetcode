"""
Difficulty : Easy
Date created : 17-11-2024
"""

import heapq


# class KthLargest:

#     def __init__(self, k: int, nums: list[int]):
#         self.k = k
#         self.nums = sorted(nums)

#     def add(self, val: int) -> int:

#         self.nums.append(val)
#         self.nums.sort()

#         return self.nums[-self.k]


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


def main():

    # kthLargest = KthLargest(3, [1, 2, 3, 3])
    # print(kthLargest.add(3))  # return 3
    # print(kthLargest.add(5))  # return 3
    # print(kthLargest.add(6))  # return 3
    # print(kthLargest.add(7))  # return 5
    # print(kthLargest.add(8))  # return 6

    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(10))
    print(kthLargest.add(9))
    print(kthLargest.add(4))

    return None


if __name__ == "__main__":
    main()

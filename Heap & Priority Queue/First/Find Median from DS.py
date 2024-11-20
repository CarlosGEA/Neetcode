"""
Difficulty : Hard
Date created : 20-11-2024
"""


class MedianFinder:
    def __init__(self):
        self.nums = []
        # self.medians = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

        self.nums.sort()
        # have queue of 2/3 nums
        # if list is even, return middle # [12456] :[245] if new num < mid find mean of mid - 1, mid else mid, mid+1
        # if list is odd return return middle
        # remove from queu appropriately

        return None

    def findMedian(self) -> float:

        n = len(self.nums) // 2
        if len(self.nums) % 2 == 1:
            return self.nums[n]

        return (self.nums[n - 1] + self.nums[n]) / 2


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

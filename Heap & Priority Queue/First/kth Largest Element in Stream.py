"""
Difficulty : Easy
Date created : 14-11-2024
"""


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:

        self.nums.append(val)
        self.nums.sort()

        return self.nums[-self.k]


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

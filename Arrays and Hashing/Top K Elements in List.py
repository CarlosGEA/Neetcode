"""
Difficulty : Medium
Date created : 11-10-2024
Status - Good?
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = {}
        for n in nums:
            frequency[n] = 1 + frequency.get(n, 0)

        frequency_descending = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
        return list(frequency_descending.keys())[:k]


def main():

    solution = Solution()

    nums = [1, 2, 2, 3, 3, 3]
    k = 2
    print(f"The {k} most common elements in array are {solution.topKFrequent(nums, k)}")

    nums = [7, 7]
    k = 1
    print(f"The {k} most common elements in array are {solution.topKFrequent(nums, k)}")

    return None


if __name__ == "__main__":
    main()

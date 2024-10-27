"""
Difficulty : Medium
Date created : 26-10-2024
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = [[] for _ in range(len(nums) + 1)]
        for key, c in count.items():
            freq[c].append(key)

        res = []
        for n in range(len(freq) - 1, -1, -1):
            for f in freq[n]:
                res.append(f)
                if len(res) == k:
                    return res


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

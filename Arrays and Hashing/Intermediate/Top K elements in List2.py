"""
Difficulty : Medium
Date created : 16-10-2024
"""

import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        res = []
        # for n, c in count.items():
        #     heapq.heappush(res, (c, n))
        #     if len(res) > k:
        #         heapq.heappop(res)


        # Bucket sort or another form of heap
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq) -1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
        return [i[1] for i in res]


def main():

    solution = Solution()

    nums = [1, 2, 2, 3, 3, 3]
    k = 2
    print(f"The {k} most frequent elements in the input array is {solution.topKFrequent(nums, k)}")

    nums = [7, 7]
    k = 1
    print(f"The {k} most frequent elements in the input array is {solution.topKFrequent(nums, k)}")

    nums = [3, 0, 1, 0]
    k = 1
    print(f"The {k} most frequent elements in the input array is {solution.topKFrequent(nums, k)}")

    return None


if __name__ == "__main__":
    main()

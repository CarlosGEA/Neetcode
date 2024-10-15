"""
Difficulty : Medium
Date created : 14-10-2024
"""
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        count = Counter(nums)
        # Same thing
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)


        res = []
        for num in count:
            if len(res) < k:
                heapq.heappush(res, (count[num], num))
            elif count[num] > res[0][0]:
                heapq.heappushpop(res, (count[num], num))

        return [i[1] for i in res]
        

def main():

    solution = Solution()


    nums = [1,2,2,3,3,3]
    k = 2
    print(f"The {k} most frequent elements in the input array is {solution.topKFrequent(nums, k)}")

    nums = [7,7]
    k = 1
    print(f"The {k} most frequent elements in the input array is {solution.topKFrequent(nums, k)}")

    nums=[3,0,1,0]
    k=1
    print(f"The {k} most frequent elements in the input array is {solution.topKFrequent(nums, k)}")


    return None


if __name__ == "__main__":
    main()
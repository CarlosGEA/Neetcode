"""
Difficulty : Medium
Date created : 19-10-2024
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
            
        
        res = []
        for idx in range(len(freq) - 1, -1, -1):
            for n in freq[idx]:
                res.append(n)
                if len(res) == k:
                    return res
        return None
        

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
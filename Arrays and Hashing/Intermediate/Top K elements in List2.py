"""
Difficulty : Medium
Date created : 14-10-2024
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Bucket sort or another form of heap
        # Don't use counter

        return 
        

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
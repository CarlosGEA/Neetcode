"""
Difficulty : Easy
Date created : 17-12-2024
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        for i in range(1, len(nums)):
            nums[i] ^= nums[i-1]
            
        return nums[-1]

def main():

    solution = Solution()

    nums = [3,2,3]
    print(f"The non repeat number in the array is {solution.singleNumber(nums)}")

    nums = [7,6,6,7,8]
    print(f"The non repeat number in the array is {solution.singleNumber(nums)}")
   
    return None


if __name__ == "__main__":
    main()
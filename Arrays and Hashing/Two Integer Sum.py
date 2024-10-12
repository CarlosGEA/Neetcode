"""
Difficulty : Easy
Date created : 10-10-2024
Status - Good
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

def main():

    solution = Solution()

    nums = [3,4,5,6]
    target = 7
    print(f"The two integer sum for target number {target} has indices: {solution.twoSum(nums, target)}")

    nums = [4,5,6]
    target = 10
    print(f"The two integer sum for target number {target} has indices: {solution.twoSum(nums, target)}")

    nums = [5,5]
    target = 10
    print(f"The two integer sum for target number {target} has indices: {solution.twoSum(nums, target)}")
   
    return None


if __name__ == "__main__":
    main()
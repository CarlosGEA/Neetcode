"""
Difficulty : Easy
Date created : 14-10-2024
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        to_find = {}
        for idx in range(n):
            if target - nums[idx] in to_find:
                return [to_find[target - nums[idx]], idx]
            to_find[nums[idx]] = idx






def main():
    
    solution = Solution()

    nums = [3,4,5,6]
    target = 7
    print(f"The index of the numbers that make the target sum {target} is {solution.twoSum(nums, target)}")


    nums = [4,5,6]
    target = 10
    print(f"The index of the numbers that make the target sum {target} is {solution.twoSum(nums, target)}")


    nums = [5,5]
    target = 10
    print(f"The index of the numbers that make the target sum {target} is {solution.twoSum(nums, target)}")

   
    return None


if __name__ == "__main__":
    main()
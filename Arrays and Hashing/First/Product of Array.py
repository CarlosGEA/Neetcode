"""
Difficulty : Medium
Date created : 12-10-2024
Status - Good
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total_prod = 1
        zeros = []
        for n in range(len(nums)):
            if nums[n] != 0:
                total_prod *= nums[n]
            else:
                zeros.append(n)


        if len(zeros) == 1:
            prod = [0] * len(nums)
            for idx in range(len(zeros)):
                prod[zeros[idx]] = total_prod
                
        elif len(zeros) > 1:
            return [0] * len(nums)
        else:
            prod = [total_prod] * len(nums)
            for idx in range(len(nums)):
                prod[idx] //= nums[idx]

        return prod


def main():

    solution = Solution()

    nums = [1,2,4,6]
    print(f"The output array for product sums disincluding self is {solution.productExceptSelf(nums)}")

    nums = [-1,0,1,2,3]
    print(f"The output array for product sums disincluding self is {solution.productExceptSelf(nums)}")
   
    return None


if __name__ == "__main__":
    main()
"""
Difficulty : Easy
Date created : 22-10-2024
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # sliding window/ two pointer
        maxp = 0
        
        for i, p in enumerate(prices):
            check_arr = sorted(prices[i:])
            max_newp = check_arr[-1]
            
            maxp = max(maxp, max_newp - p)
        return maxp
    

def main():

    solution = Solution()

    prices = [10,1,5,6,7,1]
    print(f"The max profit that can be made is {solution.maxProfit(prices)}")

    prices = [10,8,7,5,2]
    print(f"The max profit that can be made is {solution.maxProfit(prices)}")
   
    return None


if __name__ == "__main__":
    main()
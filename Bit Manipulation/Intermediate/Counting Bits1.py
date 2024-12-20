"""
Difficulty : Easy
Date created : 20-12-2024
"""

class Solution:
    def countBits(self, n: int) -> int:
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, len(dp)):
            if i == offset * 2:
                offset *= 2

            dp[i] = dp[i - offset] + 1

        return dp

def main():

    solution = Solution()
    
    n = 4
    print(f"The number of 1 bits in every digit up to {n} is {solution.countBits(n)}")
   
    return None


if __name__ == "__main__":
    main()
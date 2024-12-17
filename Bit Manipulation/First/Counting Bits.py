"""
Difficulty : Easy
Date created : 17-12-2024
"""

class Solution:
    def countBits(self, n: int) -> int:
        res = [None] * (n + 1)

        for i in range(n+1):
            res[i] = bin(i).count("1")

        return res

def main():

    solution = Solution()
    
    n = 4
    print(f"The number of 1 bits in every digit up to {n} is {solution.countBits(n)}")
   
    return None


if __name__ == "__main__":
    main()
"""
Difficulty : Medium
Date created : 18-12-2024
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Can't use + or - operators

        if b == 0:
            return a
        
        carry = (a & b) << 1
        return self.getSum(a ^ b, carry)
      

def main():

    solution = Solution()
    a = 1
    b = 1
    print(f"The sum of {a} and {b} is {solution.getSum(a,b)}")

    a = 4
    b = 7
    print(f"The sum of {a} and {b} is {solution.getSum(a,b)}")

    return None


if __name__ == "__main__":
    main()

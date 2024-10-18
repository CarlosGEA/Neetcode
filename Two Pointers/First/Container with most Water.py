"""
Difficulty : Medium
Date created : 18-10-2024
"""

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_area = 0
        while l < r:
            minh = min(heights[l], heights[r])
            max_area = max(max_area, minh * (r - l))
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area

def main():

    solution = Solution()

    height = [1,7,2,5,4,7,3,6]
    print(f"The max area of water for {height} is {solution.maxArea(height)}")

    height = [2,2,2]
    print(f"The max area of water for {height} is {solution.maxArea(height)}")

   
    return None


if __name__ == "__main__":
    main()



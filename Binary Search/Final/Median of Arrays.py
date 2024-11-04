"""
Difficulty : Hard
Date created : 03-11-2024
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        A = nums1
        B = nums2

        if len(A) > len(B):
            A, B = B, A


        l = 0 
        r = len(A) - 1

        total = len(A) + len(B)
        half = total // 2

        while True:
            m = (l + r) // 2
            i = half - m - 2

            leftA = A[m] if m >= 0 else float("-inf")
            rightA = A[m + 1] if (m + 1) < len(A) else float("inf")
            leftB = B[i] if i >= 0 else float("-inf")
            rightB = B[i + 1] if (i + 1) < len(B) else float("inf")


            if leftA <= rightB and leftB <= rightA:

                if total % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2

                else:
                     return min(rightA, rightB)

            elif leftA > rightB:
                r = m - 1
            
            else:
                l = m + 1
            

def main():

    solution = Solution()

    nums1 = [1, 2]
    nums2 = [2]
    print(f"The median of the two arrays is {solution.findMedianSortedArrays(nums1, nums2)}")

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(f"The median of the two arrays is {solution.findMedianSortedArrays(nums1, nums2)}")

    return None


if __name__ == "__main__":
    main()

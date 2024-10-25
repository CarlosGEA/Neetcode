"""
Difficulty : Hard
Date created : 21-10-2024
New Attempt : 25-10-2024
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2
        l = 0
        r = len(nums1) - 1

        while True:
            m = (l + r) // 2
            m2 = half - m - 2

            leftN1 = nums1[m] if m >= 0 else float("-inf")
            leftN2 = nums2[m2] if m2 >= 0 else float("-inf")
            rightN1 = nums1[m + 1] if (m + 1) < len(nums1) else float("inf")
            rightN2 = nums2[m2 + 1] if (m2 + 1) < len(nums2) else float("inf")
            # subarrays : nums1[l:m+1], total - m+1 - l
            if leftN2 <= rightN1 and leftN1 <= rightN2:
                if total % 2 != 0:
                    return min(rightN1, rightN2)

                else:
                    return (max(leftN1, leftN2) + min(rightN1, rightN2)) / 2
            elif leftN2 > rightN1:
                l = m + 1
            else:
                r = m - 1


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

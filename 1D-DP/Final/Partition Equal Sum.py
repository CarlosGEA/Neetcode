"""
Difficulty : Medium
Date created : 18-01-2025
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        half = sum(nums) // 2
        poss = {0}
        for num in nums:
            dummy = poss.copy()

            for n in poss:
                if n + num == half:
                    return True
                elif n + num <= half:
                    dummy.add(n + num)
            poss = dummy

        return False


def main():

    solution = Solution()

    nums = [1, 2, 3, 4]
    print(f"The nums can be partitioned : {solution.canPartition(nums)}")

    nums = [1, 2, 3, 4, 5]
    print(f"The nums can be partitioned : {solution.canPartition(nums)}")

    return None


if __name__ == "__main__":
    main()

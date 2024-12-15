"""
Difficulty : Medium
Date created : 15-12-2024
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # hash set store sums that can be made
        total = sum(nums)

        if total % 2 != 0:
            return False

        half = total // 2

        possSums = {0}
        for n in nums:
            newSet = possSums.copy()
            for s in possSums:
                newSum = s + n
                if newSum == half:
                    return True
                newSet.add(newSum)

            possSums = newSet
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

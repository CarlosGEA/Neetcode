"""
Difficulty : Medium
Date created : 11-12-2024
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        num_sum = sum(nums)
        if num_sum % 2 != 0:
            return False

        half = num_sum / 2
        nums.sort(reverse=True)

        def dfs(i, cur):
            if cur == half:
                return True

            for j in range(i, len(nums)):
                if cur + nums[j] <= half:
                    return dfs(j + 1, cur + nums[j])

            return False

        return dfs(0, 0)


def main():

    solution = Solution()

    nums = [1, 2, 3, 4]
    print(f"The nums can be partitioned : {solution.canPartition(nums)}")

    nums = [1, 2, 3, 4, 5]
    print(f"The nums can be partitioned : {solution.canPartition(nums)}")

    return None


if __name__ == "__main__":
    main()

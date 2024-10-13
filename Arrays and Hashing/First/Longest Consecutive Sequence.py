"""
Difficulty : Medium
Date created : 13-10-2024
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(set(nums))
        n = len(nums)
        if n < 2:
            return n

        longest = 1
        curr = 1
        for idx in range(n - 1):
            if nums[idx] + 1 == nums[idx + 1]:
                curr += 1
            else:
                longest = max(curr, longest)
                curr = 1

        longest = max(curr, longest)
        return longest


def main():

    solution = Solution()

    nums = [2, 20, 4, 10, 3, 4, 5]
    print(f"The largest consecutive sequence is size : {solution.longestConsecutive(nums)}")

    nums = [0, -1]
    print(f"The largest consecutive sequence is size : {solution.longestConsecutive(nums)}")

    return None


if __name__ == "__main__":
    main()

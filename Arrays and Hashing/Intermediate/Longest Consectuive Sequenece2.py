"""
Difficulty : Medium
Date created : 17-10-2024
"""


class Solution:
    def longestConsectuive(self, nums: list[int]) -> int:
       # Either work with furthest left going up
       # Use purely maps
        max_seq = 0
        for i in nums:
            start = i + 1

            if i - 1 not in nums:
                while start in nums:
                    start += 1

            max_seq = max(max_seq, start - i)

        return max_seq



def main():

    solution = Solution()

    nums = [1, -8, 7, -2, -4, -4, 6, 3, -4, 0, -7, -1, 5, 1, -9, -3]  # [2, 20, 4, 10, 3, 4, 5]
    print(f"The longest consecutive sequence in this list is {solution.longestConsectuive(nums)}")

    nums = [0, 3, 2, 5, 4, 6, 1, 1]
    print(f"The longest consecutive sequence in this list is {solution.longestConsectuive(nums)}")

    return None


if __name__ == "__main__":
    main()

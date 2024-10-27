"""
Difficulty : Medium
Date created : 26-10-2024
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        res = 0
        nums = set(nums)

        numMap = {}
        for n in nums:
            numMap[n] = 1 + numMap.get(n - 1, 0) + numMap.get(n + 1, 0)
            numMap[n - numMap.get(n - 1, 0)] = numMap[n]
            numMap[n + numMap.get(n + 1, 0)] = numMap[n]

            res = max(res, numMap[n])
        return res


def main():

    solution = Solution()

    nums = [2, 20, 4, 10, 3, 4, 5]
    print(f"The largest consecutive sequence is size : {solution.longestConsecutive(nums)}")

    nums = [0, -1]
    print(f"The largest consecutive sequence is size : {solution.longestConsecutive(nums)}")

    return None


if __name__ == "__main__":
    main()

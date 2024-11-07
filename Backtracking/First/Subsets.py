"""
Difficulty : Medium
Date created : 07-11-2024
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        for i in range(len(nums)):
            for s in range(len(res)):
                news = [i for i in res[s]]
                news.append(nums[i])
                res.append(news)
        return res


def main():

    solution = Solution()

    nums = [1, 2, 3]
    print(f"The subsets of nums are {solution.subsets(nums)}")

    nums = [7]
    print(f"The subsets of nums are {solution.subsets(nums)}")

    return None


if __name__ == "__main__":
    main()

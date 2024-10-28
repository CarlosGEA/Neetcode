"""
Difficulty : Medium
Date created : 28-10-2024
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:

            twosum = numbers[l] + numbers[r]

            if twosum == target:
                return [l + 1, r + 1]

            elif twosum > target:
                r -= 1

            else:
                l += 1


def main():

    solution = Solution()

    numbers = [1, 2, 3, 4]
    target = 3
    print(f"The is {solution.twoSum(numbers, target)}")

    return None


if __name__ == "__main__":
    main()

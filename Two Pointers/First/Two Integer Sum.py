"""
Difficulty : Medium
Date created : 17-10-2024
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Basically done, just make it nicer
        left = 0
        right = len(numbers) - 1
        while left < right:
            while numbers[left] + numbers[right] > target:
                right -= 1

            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            else:
                left += 1


def main():

    solution = Solution()

    numbers = [1, 2, 3, 4]
    target = 3
    print(f"The is {solution.twoSum(numbers, target)}")

    return None


if __name__ == "__main__":
    main()

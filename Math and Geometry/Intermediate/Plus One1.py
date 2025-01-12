"""
Difficulty : Easy
Date created : 12-01-2025
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # can optimise
        add = True
        for i in range(len(digits) - 1, -1, -1):
            if add:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    return digits

        return [1] + digits


def main():

    solution = Solution()

    digits = [1, 2, 3, 4]
    print(f"Adding 1 to this number gives {solution.plusOne(digits)}")

    digits = [9, 9, 9]
    print(f"Adding 1 to this number gives {solution.plusOne(digits)}")

    return None


if __name__ == "__main__":
    main()

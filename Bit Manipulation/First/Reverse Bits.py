"""
Difficulty : Easy
Date created : 17-12-2024
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        rev_str_n = str(format(n, '032b'))[::-1]
        print(rev_str_n)

        return int(rev_str_n, 2)


def main():

    solution = Solution()

    n = 0b00000000000000000000000000010101
    print(f"The bit reversed number of {int(n)} is {solution.reverseBits(n)} ")

    return None


if __name__ == "__main__":
    main()

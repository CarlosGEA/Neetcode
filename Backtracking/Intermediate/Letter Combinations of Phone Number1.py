"""
Difficulty : Medium
Date created : 15-11-2024
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        keys = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []

        res = [""]
        for num in digits:
            tmp = []
            for comb in res:
                for l in keys[num]:
                    tmp.append(comb + l)
            res = tmp
        return res


def main():

    solution = Solution()

    digits = "34"
    print(f"The combination of numbers for {digits} is {solution.letterCombinations(digits)}")

    digits = ""
    print(f"The combination of numbers for {digits} is {solution.letterCombinations(digits)}")

    return None


if __name__ == "__main__":
    main()

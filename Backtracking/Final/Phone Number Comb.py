"""
Difficulty : Medium
Date created : 26-11-2024
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        if not digits:
            return []

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

        res = [""]
        for n in digits:
            cur = []
            for comb in res:
                for l in keys[n]:
                    cur.append(comb + l)

            res = cur

        return res


def main():

    solution = Solution()

    digits = "34"
    print(f"The possible letter combinations of {digits} is {solution.letterCombinations(digits)}")

    digits = ""
    print(f"The possible letter combinations of {digits} is {solution.letterCombinations(digits)}")

    return None


if __name__ == "__main__":
    main()

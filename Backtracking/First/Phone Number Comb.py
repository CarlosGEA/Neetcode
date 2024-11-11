"""
Difficulty : Medium
Date created : 11-11-2024
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        keys = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        res = []

        def backtrack(cur, i):
            if i >= len(digits):
                res.append("".join(cur.copy()))
                return

            for letter in keys[int(digits[i])]:
                cur.append(letter)
                backtrack(cur, i + 1)
                cur.pop()
        if digits:
            backtrack([], 0)
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

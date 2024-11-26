"""
Difficulty : Medium
Date created : 26-11-2024
"""


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        res = []
        cur = []
        candidates.sort()

        def backtrack(i, tot):

            if tot == target:
                res.append(cur.copy())
                return

            for j in range(i, len(candidates)):

                if tot + candidates[j] > target:
                    break

                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                cur.append(candidates[j])
                backtrack(j + 1, tot + candidates[j])
                cur.pop()

        backtrack(0, 0)

        return res


def main():
    solution = Solution()

    candidates = [9, 2, 2, 4, 6, 1, 5]
    target = 8
    print(
        f"The combinations that sum to {target} are {solution.combinationSum2(candidates, target)}"
    )

    candidates = [1, 2, 3, 4, 5]
    target = 7
    print(
        f"The combinations that sum to {target} are {solution.combinationSum2(candidates, target)}"
    )

    return None


if __name__ == "__main__":
    main()

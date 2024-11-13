"""
Difficulty : Medium
Date created : 12-11-2024
"""

# save index,running total, current list


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def backtrack(i, cur, tot):
            if tot == target:
                res.append(cur.copy())
                # res.add(tuple(cur.copy()))
                return
            
            if tot > target or i == len(candidates):
                return


            for j in range(i, len(candidates)):

                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                if candidates[j] + tot <= target:
                    cur.append(candidates[j])
                    backtrack(j + 1, cur, tot + candidates[j])
                    cur.pop()
                else:
                    break


            

        backtrack(0, [], 0)
        # return [list(p) for p in res]
        return res


def main():

    solution = Solution()

    candidates = [9, 2, 2, 4, 6, 1, 5]
    target = 8
    print(
        f"The set of numbers that sum to {target} are {solution.combinationSum2(candidates, target)}"
    )

    candidates = [1, 2, 3, 4, 5]
    target = 7
    print(
        f"The set of numbers that sum to {target} are {solution.combinationSum2(candidates, target)}"
    )

    return None


if __name__ == "__main__":
    main()

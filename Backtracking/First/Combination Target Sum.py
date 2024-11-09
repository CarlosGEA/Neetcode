"""
Difficulty : Medium
Date created : 09-11-2024
"""


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = set()
        candidates.sort()
        def backtrack(candidates, potential):
            
            if not candidates:
                return
            num = candidates[0]
            
            # for p in potential:
            p_copy = potential.copy()
            p_copy.append(num)
            if sum(p_copy) == target:
                res.add(tuple(p_copy))
            elif sum(p_copy) < target:
                backtrack(candidates[1:], p_copy)
            
            backtrack(candidates[1:], potential)
            backtrack(candidates[1:], [num])
            return None
        
        backtrack(candidates, [])
        return [list(sol) for sol in res]


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

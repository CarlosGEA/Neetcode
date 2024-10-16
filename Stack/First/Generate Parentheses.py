"""
Difficulty : Medium
Date created : 15-10-2024
"""
import time

t0 = time.time()

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        bracket = "()"
        res = {"()"}
        for _ in range(2, n + 1):
            temp_res = set()
            for comb in res:
                for x in range(1, len(comb) + 1):
                    temp_res.add(comb[:x] + bracket + comb[x:])
            res = temp_res
        return res


def main():

    solution = Solution()

    n = 10
    ans = solution.generateParenthesis(n)
    print(f"From {n} brackets we can make {len(ans)}")

    return None


if __name__ == "__main__":
    main()

t1 = time.time()
print(t1-t0)


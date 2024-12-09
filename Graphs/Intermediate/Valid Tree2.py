"""
Difficulty : Medium
Date created : 09-12-2024
"""


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:

        adj_list = [[] for _ in range(n)]

        for e1, e2 in edges:
            adj_list[e1].append(e2)
            adj_list[e2].append(e1)

        def dfs(edge, pre):
            if edge in seen:
                return False

            seen.add(edge)
            for new_edge in adj_list[edge]:
                if new_edge == pre:
                    continue
                if not dfs(new_edge, edge):
                    return False
            return True

        seen = set()
        return dfs(0, -1) and len(seen) == n



def main():

    solution = Solution()

    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(f"This is a valid tree : {solution.validTree(n, edges)}")

    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(f"This is a valid tree : {solution.validTree(n, edges)}")

    return None


if __name__ == "__main__":
    main()

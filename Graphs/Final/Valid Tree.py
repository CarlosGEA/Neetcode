"""
Difficulty : Medium
Date created : 15-01-2025
"""


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # make sure all nodes are seen in one traversal
        adjDict = {i: [] for i in range(n)}
        for e1, e2 in edges:
            adjDict[e1].append(e2)
            adjDict[e2].append(e1)

        visited = set()
        seen = set()

        def dfs(edge, prev):
            if edge in seen:
                return False

            if edge in visited:
                return True

            seen.add(edge)
            for new_edge in adjDict[edge]:
                if prev != new_edge and not dfs(new_edge, edge):
                    return False

            seen.remove(edge)
            visited.add(edge)
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n


def main():

    solution = Solution()

    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(f"These edges from a valid graph? : {solution.validTree(n, edges)}")

    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(f"These edges from a valid graph? : {solution.validTree(n, edges)}")

    n = 5
    edges = [[0, 1], [2, 1], [3, 2], [3, 1], [4, 1]]
    print(f"These edges from a valid graph? : {solution.validTree(n, edges)}")

    return None


if __name__ == "__main__":
    main()

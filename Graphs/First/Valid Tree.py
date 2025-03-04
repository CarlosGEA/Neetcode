"""
Difficulty : Medium
Date created : 02-12-2024
New attempt :
"""


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:

        graphMap = {i: [] for i in range(n)}

        for head, root in edges:
            if head > root:
                head, root = root, head
            graphMap[head].append(root)

        def dfs(node):
            if node in seen:
                return False

            if graphMap[node] == []:
                seen.add(node)
                return True

            seen.add(node)
            for branch in graphMap[node]:
                if not dfs(branch):
                    return False
            graphMap[node] = []
            return True

        seen = set()
        return dfs(0) and len(seen) == n


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

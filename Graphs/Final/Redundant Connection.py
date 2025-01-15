"""
Difficulty : Medium
Date created : 15-01-2025
"""


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # union question
        n = len(edges) + 1
        rank = [1] * n
        parent = [i for i in range(n)]

        def find(node):
            par = parent[node]

            while par != parent[par]:
                parent[par] = parent[parent[par]]
                par = parent[par]

            return par

        def union(e1, e2):
            n1 = find(e1)
            n2 = find(e2)

            if n1 == n2:
                return True

            if rank[n1] >= rank[n2]:
                parent[n2] = parent[n1]
                rank[n1] += rank[n2]

            elif rank[n2] > rank[n1]:
                parent[n1] = parent[n2]
                rank[n2] += rank[n1]

            return False

        for e1, e2 in edges:
            if union(e1, e2):
                return [e1, e2]


def main():

    solution = Solution()

    # edges = [[9, 10], [5, 8], [2, 6], [1, 5], [3, 8], [4, 9], [8, 10], [4, 10], [6, 8], [7, 9]]
    # print(f"The redundant connection is {solution.findRedundantConnection(edges)}")

    edges = [[1, 5], [3, 4], [3, 5], [4, 5], [2, 4]]
    print(f"The redundant connection is {solution.findRedundantConnection(edges)}")

    return None


if __name__ == "__main__":
    main()

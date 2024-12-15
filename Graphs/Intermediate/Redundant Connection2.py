"""
Difficulty : Medium
Date created : 15-12-2024
"""


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:

        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            par = parent[n]
            while par != parent[par]:
                parent[par] = parent[parent[par]]
                par = parent[par]
            return par

        def union(n1, n2):
            n1, n2 = find(n1), find(n2)

            if n1 == n2:
                return True

            elif rank[n1] > rank[n2]:
                parent[n2] = n1
                rank[n1] += rank[n2]

            else:
                parent[n1] = n2
                rank[n2] += n1

            return False

        for e1, e2 in edges:
            if union(e1, e2):
                return [e1, e2]


def main():
    solution = Solution()

    edges = [[9, 10], [5, 8], [2, 6], [1, 5], [3, 8], [4, 9], [8, 10], [4, 10], [6, 8], [7, 9]]
    print(f"The redundant connection is {solution.findRedundantConnection(edges)}")

    edges = [[1, 2], [1, 3], [3, 4], [2, 4]]
    print(f"The redundant connection is {solution.findRedundantConnection(edges)}")

    edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
    print(f"The redundant connection is {solution.findRedundantConnection(edges)}")

    return None


if __name__ == "__main__":
    main()

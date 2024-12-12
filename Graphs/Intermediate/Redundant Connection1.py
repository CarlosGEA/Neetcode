"""
Difficulty : Medium
Date created : 09-12-2024
New attempt : 12-12-2024
"""


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:

        rank = [1] * (len(edges) + 1)
        parent = [i for i in range(len(edges) + 1)]

        def find(edge):
            par = parent[edge]
            while par != parent[par]:
                parent[par] = parent[parent[par]]
                par = parent[par]

            return par

        def union(e1, e2):

            par1, par2 = find(e1), find(e2)
            if par1 == par2:
                return False

            if rank[par1] < rank[par2]:
                parent[par2] = par1
                rank[par2] = rank[par1]

            else:
                parent[par1] = par2
                rank[par1] = rank[par2]

            return True

        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2]

        return


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

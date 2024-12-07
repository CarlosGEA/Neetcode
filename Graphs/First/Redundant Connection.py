"""
Difficulty : 
Date created : 06-12-2024
"""


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        count = {i: 0 for i in range(1, len(edges) + 1)}
        links = {i: set() for i in range(1, len(edges) + 1)}
        for e1, e2 in edges:
            count[e1] += 1
            count[e2] += 1
            links[e1].add(e2)
            links[e2].add(e1)

        mult = set()
        for val, c in count.items():
            if c > 1:
                mult.add(val)

        def dfs(n, pre):

            nonlocal e1
            nonlocal e2

            if n in seen:
                return False

            if n == e2 and pre != e1:
                return True

            seen.add(n)
            for s in links[n]:
                if s == pre:
                    continue
                if dfs(s, n):
                    return True
            seen.remove(n)

            return False

        for e1, e2 in edges[::-1]:
            if e1 in mult and e2 in mult:
                seen = set()
                if dfs(e1, -1):
                    return [e1, e2]


def main():

    solution = Solution()

    edges = [[9, 10], [5, 8], [2, 6], [1, 5], [3, 8], [4, 9], [8, 10], [4, 10], [6, 8], [7, 9]]
    print(f"The redundant connection is {solution.findRedundantConnection(edges)}")

    return None


if __name__ == "__main__":
    main()

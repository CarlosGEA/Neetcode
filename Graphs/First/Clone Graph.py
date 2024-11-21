"""
Difficulty : Medium
Date created : 21-11-2024
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def listToGraph(adjList):
    if not adjList:
        return None

    nodeMap = {i + 1: Node(i + 1) for i in range(len(adjList))}

    for i, neighbors in enumerate(adjList):
        nodeMap[i + 1].neighbors = [nodeMap[neighbor] for neighbor in neighbors]

    return nodeMap[1]


def graphToList(node):
    if not node:
        return []

    adjList = {}
    visited = set()

    def dfs(current):
        if current.val in visited:
            return
        visited.add(current.val)
        adjList[current.val] = [neighbor.val for neighbor in current.neighbors]
        for neighbor in current.neighbors:
            dfs(neighbor)

    dfs(node)

    max_index = max(adjList.keys())
    result = [adjList.get(i, []) for i in range(1, max_index + 1)]
    return result


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:

        if not node:
            return None

        adjList = {}
        visited = set()

        def dfs(current):
            if current.val in visited:
                return
            visited.add(current.val)
            adjList[current] = Node(current.val)
            for neighbor in current.neighbors:
                dfs(neighbor)

        dfs(node)

        visited = set()

        def dfs(current):
            if adjList[current] in visited:
                return

            visited.add(adjList[current])

            adjList[current].neighbors = [adjList[neighbor] for neighbor in current.neighbors]
            for neighbor in current.neighbors:
                dfs(neighbor)

        dfs(node)

        return adjList[node]


def main():

    solution = Solution()

    adjList = [[2], [1, 3], [2]]
    print(f"The cloned graph is {graphToList(solution.cloneGraph(listToGraph(adjList)))}")

    adjList = [[]]
    print(f"The cloned graph is {graphToList(solution.cloneGraph(listToGraph(adjList)))}")

    adjList = []
    print(f"The cloned graph is {graphToList(solution.cloneGraph(listToGraph(adjList)))}")

    return None


if __name__ == "__main__":
    main()

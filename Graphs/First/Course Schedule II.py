"""
Difficulty : Medium
Date created : 02-12-2024
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()
        seen = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                if crs not in seen:
                    order.append(crs)
                    seen.add(crs)
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []

            if crs not in seen:
                order.append(crs)
                seen.add(crs)
            return True

        order = []
        for c in range(numCourses):
            if not dfs(c):
                return []

        for c in range(numCourses):
            if c not in seen:
                order.append(c)
        return order


def main():

    solution = Solution()

    numCourses=7
    prerequisites=[[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
    print(f"The order of courses possible is {solution.findOrder(numCourses, prerequisites)}")

    numCourses = 3
    prerequisites = [[0, 1], [1, 2], [2, 0]]
    print(f"The order of courses possible is {solution.findOrder(numCourses, prerequisites)}")

    numCourses = 2
    prerequisites = [[0, 1]]
    print(f"The order of courses possible is {solution.findOrder(numCourses, prerequisites)}")

    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(f"The order of courses possible is {solution.findOrder(numCourses, prerequisites)}")

    return None


if __name__ == "__main__":
    main()

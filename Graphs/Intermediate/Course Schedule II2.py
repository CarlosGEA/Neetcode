"""
Difficulty : Medium
Date created : 10-12-2024
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        courseMap = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            courseMap[c].append(p)

        def dfs(course):
            if course in seen:
                return False

            if course in visited:
                return True

            seen.add(course)
            for nc in courseMap[course]:
                if not dfs(nc):
                    return False

            seen.remove(course)
            res.append(course)
            visited.add(course)
            return True

        res = []
        seen = set()
        visited = set()

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res


def main():

    solution = Solution()

    numCourses = 7
    prerequisites = [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]
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

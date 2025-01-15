"""
Difficulty : Medium
Date created : 15-01-2025
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # make sure to account for case where its not possible
        preDict = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preDict[course].append(pre)

        seen = set()
        res = []

        def dfs(c):
            if c in seen:
                return False
            if c not in preDict:
                return True

            seen.add(c)
            for pre in preDict[c]:
                if not dfs(pre):
                    return False
            seen.remove(c)
            res.append(c)
            del preDict[c]
            return True

        for i in range(numCourses):
            if not dfs(i):
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

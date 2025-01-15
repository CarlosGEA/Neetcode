"""
Difficulty : Medium
Date created : 15-01-2025
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # once course has been checked make it easier to know and return true if we reach it again
        preDict = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preDict[course].append(pre)

        seen = set()

        # used = set()
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
            del preDict[c]
            # used.add(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        # return len(used) == numCourses
        return True


def main():

    solution = Solution()

    numCourses = 4
    prerequisites = [[0, 1], [2, 3], [1, 2], [3, 0]]
    print(f"Is this schedule valid? : {solution.canFinish(numCourses, prerequisites)}")

    numCourses = 2
    prerequisites = [[0, 1]]
    print(f"Is this schedule valid? : {solution.canFinish(numCourses, prerequisites)}")

    numCourses = 2
    prerequisites = [[0, 1], [1, 0]]
    print(f"Is this schedule valid? : {solution.canFinish(numCourses, prerequisites)}")

    return None


if __name__ == "__main__":
    main()

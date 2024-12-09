"""
Difficulty : 
Date created : 09-12-2024
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        courseMap = {i: [] for i in range(numCourses)}

        for p, c in prerequisites:
            courseMap[p].append(c)

        seen = set()
        def dfs(course):
            if course in seen: 
                return False
            
            seen.add(course)
            for nc in courseMap[course]:
                if not dfs(nc):
                    return False
            seen.remove(course)  
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True


def main():

    solution = Solution()

    numCourses = 2
    prerequisites = [[0, 1]]
    print(f"It is possible to finish all courses : {solution.canFinish(numCourses, prerequisites)}")

    numCourses = 2
    prerequisites = [[0, 1], [1, 0]]
    print(f"It is possible to finish all courses : {solution.canFinish(numCourses, prerequisites)}")

    return None


if __name__ == "__main__":
    main()

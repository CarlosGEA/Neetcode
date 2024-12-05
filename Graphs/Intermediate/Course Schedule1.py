"""
Difficulty : Medium
Date created : 02-12-2024
New attempt : 05-12-2024
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        course_req = {i: [] for i in range(numCourses)}
        for p, c in prerequisites:
            course_req[p].append(c)

        def dfs(course):
            if course in seen:
                return False

            if course_req[course] == []:
                return True

            seen.add(course)
            for c in course_req[course]:
                if not dfs(c):
                    return False
            seen.remove(course)
            course_req[course] = []
            return True

        seen = set()
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True


def main():

    solution = Solution()

    numCourses = 2
    prerequisites = [[0, 1]]
    print(f"Is the order of courses valid? : {solution.canFinish(numCourses, prerequisites)}")

    numCourses = 2
    prerequisites = [[0, 1], [1, 0]]
    print(f"Is the order of courses valid? : {solution.canFinish(numCourses, prerequisites)}")

    return None


if __name__ == "__main__":
    main()

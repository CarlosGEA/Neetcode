"""
Difficulty : Medium
Date created : 02-12-2024
New attempt : 
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        return

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

"""
Difficulty : Medium
Date created : 29-11-2024
"""

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        if not prerequisites:
            return True

        order_dict = defaultdict(set)
        for person in prerequisites:
            for i in range(len(person)):
                if i > 0:
                    dummy = order_dict[person[i - 1]].copy()
                    for p in dummy:
                        order_dict[person[i - 1]].update(order_dict[p])

                    if person[i] in order_dict[person[i - 1]] or person[i - 1] == person[i]:
                        return False

                    order_dict[person[i]].update(order_dict[person[i - 1]])
                    order_dict[person[i]].add(person[i - 1])

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

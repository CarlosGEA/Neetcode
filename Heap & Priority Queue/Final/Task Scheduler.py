"""
Difficulty : Medium 
Date created : 04-12-2024
"""

from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        count = Counter(tasks)
        maxtask = max(count.values())

        num_max = list(count.values()).count(maxtask)

        return max((n + 1) * (maxtask - 1) + num_max, len(tasks))


def main():

    solution = Solution()

    tasks = ["X", "X", "Y", "Y"]
    n = 2
    print(
        f"The minimum number of cycles with {n} waiting period is {solution.leastInterval(tasks, n)}"
    )

    tasks = ["A", "A", "A", "B", "C"]
    n = 3
    print(
        f"The minimum number of cycles with {n} waiting period is {solution.leastInterval(tasks, n)}"
    )

    return None


if __name__ == "__main__":
    main()

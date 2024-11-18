"""
Difficulty : Medium 
Date created : 18-11-2024
"""

import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        cycle = 0

        task_last = {}  # initiliaze cycle at which last task occured
        task_freq = {}  # get frequency of tasks

        for t in tasks:
            task_last[t] = 0
            task_freq[t] = 1 + task_freq.get(t, 0)

        vals = [(-f, l) for l, f in task_freq.items()]
        heapq.heapify(vals)  # create max heap of tasks

        while vals:
            # iterate through max heap and get the task with the current highest frequency that can be complete
            i = 0
            while i < len(vals) and task_last[vals[i][1]] and cycle - task_last[vals[i][1]] < n:
                i += 1

            if i == len(
                vals
            ):  # if no tasks can be completed add an idle cycle and continue to next cycle
                cycle += 1
                continue

            # decrease frequency of task being complete and update cycle at which task last completed
            # remove task from heap
            freq, task = vals[i]
            cycle += 1
            del vals[i]
            freq += 1
            task_last[task] = cycle

            # if task still has to be complete more times add to max heao
            if freq:
                heapq.heappush(vals, (freq, task))

        return cycle


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

"""
Difficulty : Medium
Date created : 16-10-2024
"""
import heapq

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        idx = []

        # for i in range(n-1):
        #     for j in range(i + 1, n):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i
        #             break
        for i in range(n):
            heapq.heappush(idx, (temperatures[i], i))
            while temperatures[i] > idx[0][0]:
                pop_idx = heapq.heappop(idx)[1]
                res[pop_idx] = i - pop_idx

        return res


def main():

    solution = Solution()

    temperatures = [30, 38, 30, 36, 35, 40, 28]
    print(f"The result is {solution.dailyTemperatures(temperatures)}")

    temperatures = [22, 21, 20]
    print(f"The result is {solution.dailyTemperatures(temperatures)}")


    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 30-10-2024
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        stack = []  # [Temp, Idx]
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([t, i])
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

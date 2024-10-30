"""
Difficulty : Medium
Date created : 30-10-2024
"""


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        data = [i for i in zip(position, speed)]
        data.sort(reverse=True)

        for p, s in data:

            grad = (target - p) / s
            if not stack or stack[-1] < grad:
                stack.append(grad)

        return len(stack)


def main():

    solution = Solution()

    target = 10
    position = [1, 4]
    speed = [3, 2]
    print(f"The number of fleets created is {solution.carFleet(target, position, speed)}")

    target = 10
    position = [4, 1, 0, 7]
    speed = [2, 2, 1, 1]
    print(f"The number of fleets created is {solution.carFleet(target, position, speed)}")

    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(f"The number of fleets created is {solution.carFleet(target, position, speed)}")

    return None


if __name__ == "__main__":
    main()

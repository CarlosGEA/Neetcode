"""
Difficulty : Medium
Date created : 19-10-2024
"""


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # only compare gradients in stack

        info = sorted([[position[i], speed[i]] for i in range(len(speed))], reverse=True)

        fleet = []
        for i in info:

            if not fleet:
                fleet.append(i)

            if ((target - i[0]) / i[1]) > ((target - fleet[-1][0]) / fleet[-1][1]):
                fleet.append(i)

        return len(fleet)


def main():

    solution = Solution()

    target = 10
    position = [1, 4]
    speed = [3, 2]
    print(f"The number of car fleets are {solution.carFleet(target, position, speed)}")

    target = 10
    position = [4, 1, 0, 7]
    speed = [2, 2, 1, 1]
    print(f"The number of car fleets are {solution.carFleet(target, position, speed)}")

    return None


if __name__ == "__main__":
    main()

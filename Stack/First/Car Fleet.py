"""
Difficulty : Medium
Date created : 16-10-2024
"""

import heapq


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        fleet = []
        n = len(position)

        position, speed = zip(*sorted(zip(position, speed), reverse=True))
        
        fleet.append((position[0], (target - position[0]) / speed[0]))
        for i in range(1, n):
            time = (target - position[i]) / speed[i]
            for c in fleet:
                if time == c[1] or (time < c[1] and position[i] < c[0]):
                    break
            else:
                heapq.heappush(fleet, (position[i], time))

        return len(fleet)

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

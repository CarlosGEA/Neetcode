"""
Difficulty : Medium
Date created : 22-10-2024
"""

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        stack = []

        sorted_data = sorted([position[i], speed[i]] for i in range(len(speed)))[::-1]

        for c in range(len(position)):
            time = (target - sorted_data[c][0]) / sorted_data[c][1]

            if not stack or time > stack[-1]:
                stack.append(time) 
        
        return len(stack)
    

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

    target=10
    position=[0,4,2]
    speed=[2,1,3]
    print(f"The number of car fleets are {solution.carFleet(target, position, speed)}")
   
    return None


if __name__ == "__main__":
    main()
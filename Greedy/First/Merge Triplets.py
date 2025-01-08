"""
Difficulty : Medium
Date created : 08-01-2025
New attempt : 
"""


class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        

        

        return


def main():

    solution = Solution()

    triplets = [[1, 2, 3], [7, 1, 1]]
    target = [7, 2, 3]
    print(
        f"The target can be formed by the given method : {solution.mergeTriplets(triplets, target)}"
    )

    triplets = [[2, 5, 6], [1, 4, 4], [5, 7, 5]]
    target = [5, 4, 6]
    print(
        f"The target can be formed by the given method : {solution.mergeTriplets(triplets, target)}"
    )

    return None


if __name__ == "__main__":
    main()

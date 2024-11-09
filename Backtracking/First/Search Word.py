"""
Difficulty : Medium
Date created : 09-11-2024
New attempt : 
"""

from collections import defaultdict


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        return


def main():

    solution = Solution()

    # board = [["A", "B", "C", "D"], ["S", "A", "A", "T"], ["A", "C", "A", "E"]]
    # word = "CAT"
    # print(f"The word {word} can be found in the board? : {solution.exist(board, word)}")

    # board = [["A", "B", "C", "D"], ["S", "A", "A", "T"], ["A", "C", "A", "E"]]
    # word = "BAT"
    # print(f"The word {word} can be found in the board? : {solution.exist(board, word)}")

    board = [["a", "a"]]
    word = "aa"
    print(f"The word {word} can be found in the board? : {solution.exist(board, word)}")

    # board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # word="ABCB"
    # print(f"The word {word} can be found in the board? : {solution.exist(board, word)}")

    return None


if __name__ == "__main__":
    main()

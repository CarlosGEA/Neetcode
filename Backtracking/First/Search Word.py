"""
Difficulty : Medium
Date created : 09-11-2024
New attempt : 13-11-2024
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        # backtrack and store currently used letters, iterate through each letter
        ROWS = len(board)
        COLS = len(board[0])

        path = set()

        def backtrack(i, r, c):
            if i == len(word):
                return True

            letter = word[i]
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in path or board[r][c] != letter:
                return False

            path.add((r, c))

            exists = (
                backtrack(i + 1, r + 1, c)
                or backtrack(i + 1, r - 1, c)
                or backtrack(i + 1, r, c + 1)
                or backtrack(i + 1, r, c - 1)
            )

            path.remove((r,c))

            return exists

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(0, r, c):
                    return True

        return False


def main():

    solution = Solution()

    board = [["A", "B", "C", "D"], ["S", "A", "A", "T"], ["A", "C", "A", "E"]]
    word = "CAT"
    print(f"The word {word} can be found in the board? : {solution.exist(board, word)}")

    board = [["A", "B", "C", "D"], ["S", "A", "A", "T"], ["A", "C", "A", "E"]]
    word = "BAT"
    print(f"The word {word} can be found in the board? : {solution.exist(board, word)}")

    board = [["a", "a"]]
    word = "aa"
    print(f"The word {word} can be found in the board? : {solution.exist(board, word)}")

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    print(f"The word {word} can be found in the board? : {solution.exist(board, word)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 16-11-2024
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        path = set()

        rows = len(board)
        cols = len(board[0])

        def backtrack(i, pos):

            if i == len(word):
                return True

            r = pos[0]
            c = pos[1]

            if pos in path or r < 0 or r >= rows or c < 0 or c >= cols or word[i] != board[r][c]:
                return False

            path.add((r, c))

            exists = (
                backtrack(i + 1, (r + 1, c))
                or backtrack(i + 1, (r - 1, c))
                or backtrack(i + 1, (r, c + 1))
                or backtrack(i + 1, (r, c - 1))
            )

            path.remove((r, c))

            return exists

        for r in range(rows):
            for c in range(cols):
                if backtrack(0, (r, c)):
                    return True

        return False


def main():

    solution = Solution()

    # board = [["A", "B", "C", "D"], ["S", "A", "A", "T"], ["A", "C", "A", "E"]]
    # word = "CAT"
    # print(f"Can {word} be found orthogonally in board? : {solution.exist(board, word)}")

    # board = [["A", "B", "C", "D"], ["S", "A", "A", "T"], ["A", "C", "A", "E"]]
    # word = "BAT"
    # print(f"Can {word} be found orthogonally in board? : {solution.exist(board, word)}")

    board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word = "AAB"
    print(f"Can {word} be found orthogonally in board? : {solution.exist(board, word)}")

    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"
    print(f"Can {word} be found orthogonally in board? : {solution.exist(board, word)}")

    return None


if __name__ == "__main__":
    main()

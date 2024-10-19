"""
Difficulty : Medium
Date created : 19-10-2024
"""


class Solution:
    def encode(self, strs: list[str]) -> str:

        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> list[str]:
        decoded = []

        start = 0

        while start < len(s):
            end = start

            while s[end] != "#":
                end += 1
            length = int(s[start:end])
            start = end + 1
            end = start + length
            decoded.append(s[start:end])
            start = end

        return decoded


def main():

    solution = Solution()

    input = ["neet", "code", "love", "you"]
    print(solution.decode(solution.encode(input)))

    input = ["we", "say", ":", "yes"]
    print(solution.decode(solution.encode(input)))

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 11-10-2024
Status - Not complete
"""


class Solution:

    def encode(self, strs: list[str]) -> str:
        # Encode using number and #
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> list[str]:
        # Decode when finding # and length of string before that
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

    input = ["we", "say", ":", "yes", "!@#$%^&*()"]
    encoded = solution.encode(input)
    decoded = solution.decode(encoded)
    print(f"After encoding and decoding the input we get {decoded}")

    input = ["we", "say", ":", "yes"]
    encoded = solution.encode(input)
    decoded = solution.decode(encoded)
    print(f"After encoding and decoding the input we get {decoded}")

    return None


if __name__ == "__main__":
    main()

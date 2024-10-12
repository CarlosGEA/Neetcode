"""
Difficulty : Medium
Date created : 11-10-2024
Status - Not complete
"""
class Solution:

    def encode(self, strs: list[str]) -> str:
        # Encode using number and #
        return

    def decode(self, s: str) -> list[str]:
       # Decode when finding # and length of string before that
       
       return


def main():

    solution = Solution()

    # input = ["neet","code","love","you"]
    input = [""]
    encoded = solution.encode(input)
    decoded = solution.decode(encoded)
    print(f"After encoding and decoding the input we get {decoded}")


    input = ["we","say",":","yes"]
    encoded = solution.encode(input)
    decoded = solution.decode(encoded)
    print(f"After encoding and decoding the input we get {decoded}")
   
    return None


if __name__ == "__main__":
    main()
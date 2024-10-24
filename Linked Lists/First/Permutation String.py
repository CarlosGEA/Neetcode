"""
Difficulty : Medium
Date created : 24-10-2024
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check_count = {}
        s1_count = {}

        # Not bad but cant improve by sliding window of size of s1

        for c in s1:
            s1_count[c] = 1 + s1_count.get(c, 0)

        l = 0
        for r, elem in enumerate(s2):
            if check_count == s1_count:
                return True

            if elem in s1_count:
                check_count[elem] = 1 + check_count.get(elem, 0)
                l += 1

                while check_count[elem] > s1_count[elem]:
                    check_count[s2[r - l + 1]] -= 1
                    l -= 1
            else:
                check_count = {}

        return check_count == s1_count


def main():

    solution = Solution()

    s1 = "abc"
    s2 = "lecabee"
    print(f"s2 contains a substring permutation of s1? {solution.checkInclusion(s1, s2)}")

    s1 = "abc"
    s2 = "lecaabee"
    print(f"s2 contains a substring permutation of s1? {solution.checkInclusion(s1, s2)}")

    s1 = "adc"
    s2 = "dcda"
    print(f"s2 contains a substring permutation of s1? {solution.checkInclusion(s1, s2)}")

    s1 = "abc"
    s2 = "bbbca"
    print(f"s2 contains a substring permutation of s1? {solution.checkInclusion(s1, s2)}")

    return None


if __name__ == "__main__":
    main()

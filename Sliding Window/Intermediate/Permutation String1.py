"""
Difficulty : Medium
Date created : 27-10-2024
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        matches = 0
        count = {}

        for s in s1:
            count[s] = count.get(s, 0) + 1

        left = 0
        for right in range(len(s2)):

            if matches == len(count):
                return True

            if s2[right] in count:
                count[s2[right]] -= 1

                if count[s2[right]] == 0:
                    matches += 1

                elif (count[s2[right]] + 1) == 0:
                    matches -= 1

            if right < len(s1):
                continue

            if s2[left] in count:
                count[s2[left]] += 1

                if count[s2[left]] == 0:
                    matches += 1

                elif (count[s2[left]] - 1) == 0:
                    matches -= 1
            left += 1

        return matches == len(s1)


def main():

    solution = Solution()

    # s1 = "abc"
    # s2 = "lecabee"
    # print(f"s2 contains a substring permutation of s1? {solution.checkInclusion(s1, s2)}")

    # s1 = "abc"
    # s2 = "lecaabee"
    # print(f"s2 contains a substring permutation of s1? {solution.checkInclusion(s1, s2)}")

    # s1 = "adc"
    # s2 = "dcda"
    # print(f"s2 contains a substring permutation of s1? {solution.checkInclusion(s1, s2)}")

    # s1 = "abc"
    # s2 = "bbbca"
    # print(f"s2 contains a substring permutation of s1? {solution.checkInclusion(s1, s2)}")

    s1 = "trinitrophenylmethylnitramine"
    s2 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine"
    print(f"s2 contains a substring permutation of s1? {solution.checkInclusion(s1, s2)}")

    return None


if __name__ == "__main__":
    main()

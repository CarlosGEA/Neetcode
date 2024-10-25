"""
Difficulty : Medium 
Date created : 24-10-2024
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window, move left pointer once condition is not valid

        max_len = 0

        for idx, elem in enumerate(s):
            counter = {}
            right = idx
            while right < len(s):
                counter[s[right]] = counter.get(s[right], 0) + 1
                least_common_counter_vals = sorted(counter.values())
                if (len(counter) > 2 and sum(least_common_counter_vals[:-1]) > k) or (
                    len(counter) == 2 and least_common_counter_vals[0] > k
                ):
               
                    max_len = max(max_len, sum(counter.values()) - 1)
                    break
                right += 1
            if right == len(s):
                max_len = max(max_len, sum(counter.values()))
            

        return max_len


def main():

    solution = Solution()

    s = "XYYX"
    k = 2
    print(f"The longest substring is length {solution.characterReplacement(s, k)}")

    s = "AAABABB"
    k = 1
    print(f"The longest substring is length {solution.characterReplacement(s, k)}")

    return None


if __name__ == "__main__":
    main()

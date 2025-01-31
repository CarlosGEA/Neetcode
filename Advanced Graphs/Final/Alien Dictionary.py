"""
Difficulty : Hard
Date created : 31-01-2025
"""


class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        # linked list topological search
        adj = {i: set() for word in words for i in word}
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            minlen = min(len(w1), len(w2))
            if w1[:minlen] == w2[:minlen] and len(w1) > len(w2):
                return ""

            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = set()
        seen = set()

        def dfs(val):
            if val in seen:
                return False
            if val in visited:
                return True

            seen.add(val)
            for new_val in adj[val]:
                if not dfs(new_val):
                    return False
            seen.remove(val)
            visited.add(val)
            res.append(val)
            return True

        res = []
        for key in adj:
            if not dfs(key):
                return ""

        return "".join(res[::-1])


def main():

    solution = Solution()

    words = ["z", "o"]
    print(
        f"In this new language the lexicographic order of letters is {solution.foreignDictionary(words)}"
    )

    words = ["hrn", "hrf", "er", "enn", "rfnn"]
    print(
        f"In this new language the lexicographic order of letters is {solution.foreignDictionary(words)}"
    )

    words = ["abc", "bcd", "cde"]
    print(
        f"In this new language the lexicographic order of letters is {solution.foreignDictionary(words)}"
    )

    words = ["wrtkj", "wrt"]
    print(
        f"In this new language the lexicographic order of letters is {solution.foreignDictionary(words)}"
    )

    return None


if __name__ == "__main__":
    main()

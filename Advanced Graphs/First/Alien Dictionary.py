"""
Difficulty : Hard
Date created : 14-01-2025
New attempt : 17-01-2025
"""


class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        # topological sort & post-order dfs
        # this is tricky make adj list and then do dfs

        adj = {l: [] for word in words for l in word}

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                l = 0
                while l < len(words[i]) and l < len(words[j]):
                    if words[i][l] != words[j][l]:
                        adj[words[i][l]].append(words[j][l])
                        break
                    l += 1
                if l == len(words[j]) and len(words[i]) > len(words[j]):
                    return ""

        visit = set()
        processed = set()
        res = []

        def dfs(i):

            if i in processed:
                return True

            if i in visit:
                return False

            visit.add(i)
            for l in adj[i]:
                if not dfs(l):
                    return False
            visit.remove(i)
            processed.add(i)
            res.append(i)
            return True

        for l in adj.keys():
            if not dfs(l):
                return False

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

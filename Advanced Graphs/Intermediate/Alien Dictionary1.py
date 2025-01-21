"""
Difficulty : Hard
Date created : 20-01-2025
"""


class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        # good -> can make 1 loop for adj dict by going through adjacent words rather than all combos,
        # find minlen and use that to set maximum rather than while loop and to check we don't have invalid
        # order of strings
        # in dfs instead of seen and visited can have boolean for each element

        adj = {l: set() for word in words for l in word}

        for i in range(len(words) - 1):
            minLen = min(len(words[i]), len(words[i + 1]))
            if words[i][:minLen] == words[i+1][:minLen] and len(words[i]) > len(words[i+1]):
                return ""

            for k in range(minLen):
                if words[i][k] != words[i+1][k]:
                    adj[words[i][k]].add(words[i+1][k])
                    break

        visited = {} # False if seen, True if in cycle
        res = []

        def dfs(l):

            if l in visited:
                return not visited[l]

            visited[l] = True
            for new_l in adj[l]:
                if not dfs(new_l):
                    return False

            visited[l] = False
            res.append(l)
            return True

        for letter in adj:
            if not dfs(letter):
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

    words = ["wrt","wrf","er","ett","rftt","te"]
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

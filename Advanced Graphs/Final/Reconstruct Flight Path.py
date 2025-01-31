"""
Difficulty : Hard
Date created : 31-01-2025
"""

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:

        adj = defaultdict(list)

        for s, d in sorted(tickets)[::-1]:
            adj[s].append(d)

        res = []
        queue = ["JFK"]
        while queue:
            src = queue[-1]
            if adj[src]:
                queue.append(adj[src].pop())
            else:
                res.append(queue.pop())

        return res[::-1]


def main():

    solution = Solution()

    tickets = [["BUF", "HOU"], ["HOU", "SEA"], ["JFK", "BUF"]]
    print(f"The itinerary for all the tickets is {solution.findItinerary(tickets)}")

    tickets = [["HOU", "JFK"], ["SEA", "JFK"], ["JFK", "SEA"], ["JFK", "HOU"]]
    print(f"The itinerary for all the tickets is {solution.findItinerary(tickets)}")

    return None


if __name__ == "__main__":
    main()

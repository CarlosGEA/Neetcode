"""
Difficulty : Hard
Date created : 13-01-2025
"""

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:

        connections = defaultdict(list)

        for i, ticket in enumerate(tickets):
            connections[ticket[0]].append([ticket[1], i])

        current = "JFK"
        seen = set()
        res = [current]
        while len(seen) != len(tickets):

            for new_dest, ticket in sorted(connections[current]):
                if ticket in seen:
                    continue
                current = new_dest
                seen.add(ticket)
                res.append(new_dest)
                break

        return res


def main():

    solution = Solution()

    tickets = [["BUF", "HOU"], ["HOU", "SEA"], ["JFK", "BUF"]]
    print(f"The itinerary for all the tickets is {solution.findItinerary(tickets)}")

    tickets = [["HOU", "JFK"], ["SEA", "JFK"], ["JFK", "SEA"], ["JFK", "HOU"]]
    print(f"The itinerary for all the tickets is {solution.findItinerary(tickets)}")

    return None


if __name__ == "__main__":
    main()

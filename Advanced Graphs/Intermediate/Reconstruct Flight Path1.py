"""
Difficulty : Hard
Date created : 16-01-2025
New attempt : 19-01-2025
"""

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        return

def main():

    solution = Solution()

    tickets = [["BUF", "HOU"], ["HOU", "SEA"], ["JFK", "BUF"]]
    print(f"The itinerary for all the tickets is {solution.findItinerary(tickets)}")

    tickets = [["HOU", "JFK"], ["SEA", "JFK"], ["JFK", "SEA"], ["JFK", "HOU"]]
    print(f"The itinerary for all the tickets is {solution.findItinerary(tickets)}")

    tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    print(f"The itinerary for all the tickets is {solution.findItinerary(tickets)}")

    return None


if __name__ == "__main__":
    main()

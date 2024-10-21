"""
Difficulty : Medium
Date created : 21-10-2024
"""

from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        return None

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        return None

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        # implement binary search here
        for t, v in values[::-1]:
            if t <= timestamp:
                return v
        return ""


def main():

    timeMap = TimeMap()
    timeMap.set("alice", "happy", 1)
    print(timeMap.get("alice", 1))  # "happy"
    print(timeMap.get("alice", 2))  # "happy"
    timeMap.set("alice", "sad", 3)
    print(timeMap.get("alice", 3))  # "sad"

    return None


if __name__ == "__main__":
    main()

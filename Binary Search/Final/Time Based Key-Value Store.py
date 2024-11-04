"""
Difficulty : Medium
Date created : 03-11-2024
"""

from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.data[key].append([timestamp, value])
        return None

    def get(self, key: str, timestamp: int) -> str:

        res = ""
        vals = self.data[key]

        l = 0
        r = len(vals) - 1

        while l <= r:
            m = (l + r) // 2
            time = vals[m][0]
            if timestamp >= time:
                l = m + 1
                res = vals[m][1]
            else:
                r = m - 1

        return res


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

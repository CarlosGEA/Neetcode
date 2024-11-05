"""
Difficulty : Medium
Date created : 05-11-2024
"""

from collections import defaultdict


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = defaultdict(list)  # key : [val, node]

        self.last = self.first = ListNode(0, 0)  # change
        self.last.next = self.first
        self.first.prev = self.last

    def get(self, key: int) -> int:

        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        lru = self.last.next
        if len(self.cache) > self.cap:
            self.remove(lru)
            del self.cache[lru.key]
        return None

    def insert(self, node):
        most_recent = self.first.prev

        most_recent.next = node
        self.first.prev = node

        node.prev = most_recent
        node.next = self.first

        return None

    def remove(self, node):
        prevN = node.prev
        nextN = node.next

        prevN.next = nextN
        nextN.prev = prevN

        return None


def main():

    cache = LRUCache(2)
    cache.put(1, 10)  # cache: {1=10}
    print(cache.get(1))  # return 10
    cache.put(2, 20)  # cache: {1=10, 2=20}
    cache.put(3, 30)  # cache: {2=20, 3=30}, key=1 was evicted
    print(cache.get(2))  # returns 20
    print(cache.get(1))  # return -1 (not found)

    print("\nNEW\n")

    cache = LRUCache(2)
    print(cache.get(2))  # returns -1
    cache.put(2, 6)
    print(cache.get(1))  # returns -1
    cache.put(1, 5)
    cache.put(1, 2)
    print(cache.get(1))  # returns 2
    print(cache.get(2))  # returns 6

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 19-11-2024
"""


class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.first = ListNode(0, 0)
        self.last = ListNode(0, 0)
        self.first.next = self.last
        self.last.prev = self.first

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        node = ListNode(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            LRU = self.first.next
            self.remove(LRU)
            del self.cache[LRU.key]

        return None

    def insert(self, node) -> None:

        nxt = self.last
        prv = self.last.prev

        nxt.prev = prv.next = node
        node.next = nxt
        node.prev = prv

        return None

    def remove(self, node) -> None:

        nxt = node.next
        prv = node.prev

        nxt.prev = prv
        prv.next = nxt

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
    print(cache.get(2))
    cache.put(2, 6)
    print(cache.get(1))
    cache.put(1, 5)
    cache.put(1, 2)
    print(cache.get(1))
    print(cache.get(2))

    return None


if __name__ == "__main__":
    main()

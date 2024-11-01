"""
Difficulty : Medium
Date created : 01-11-2024
"""


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:

        if key in self.cache:
            self.removeKey(self.cache[key])
            self.insertKey(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.removeKey(self.cache[key])

        self.cache[key] = ListNode(key, value)
        self.insertKey(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.removeKey(lru)
            del self.cache[lru.key]

        return None

    def insertKey(self, node) -> None:
        prevN = self.right.prev
        nextN = self.right

        prevN.next = nextN.prev = node
        node.prev = prevN
        node.next = nextN

        return None

    def removeKey(self, node) -> None:

        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

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

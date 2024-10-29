"""
Difficulty : Medium
Date created : 29-10-2024
"""


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used_stack = []
        self.store = {}

    def get(self, key: int) -> int:

        val = self.store.get(key, -1)

        if val != -1:
            self.used_stack.pop(self.used_stack.index(key))
            self.used_stack.append(key)

        return val

    def put(self, key: int, value: int) -> None:

        if key in self.store:
            self.used_stack.pop(self.used_stack.index(key))

        self.store[key] = value

        self.used_stack.append(key)

        if len(self.store) > self.capacity:
            # if len(self.store) == self.capacity and key not in self.store:
            del_key = self.used_stack.pop(0)
            self.store.pop(del_key, None)

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

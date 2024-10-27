"""
Difficulty : Medium
Date created : 26-10-2024
"""


def listToArr(head):
    current = head
    arr = []
    index_map = {}
    index = 0

    # First pass to map each node to its index
    while current:
        index_map[current] = index
        current = current.next
        index += 1

    # Second pass to build the array with index references for random pointers
    current = head
    while current:
        random_index = index_map.get(current.random, None)  # Get index of the random pointer
        arr.append([current.val, random_index])
        current = current.next

    return arr


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:

        start = head
        newHead = Node(0)
        dummy = dummyRandom = newRandom = newHead
        random_val = []
        while start is not None:
            if start.random is not None:
                random_val.append(start.random.val)
            else:
                random_val.append(start.random)

            newHead.next = Node(start.val)
            start = start.next
            newHead = newHead.next
       
        for r in random_val:
            newRandom = newRandom.next
            if r == None:
                newRandom.random = r
            else:
                start = head
                dummyRandom = dummy.next
                while start.val != r:
                    start = start.next
                    dummyRandom = dummyRandom.next
                
                newRandom.random = dummyRandom
        return dummy.next


def createLinkedList(data):
    if not data:
        return None

    nodes = [Node(x[0]) for x in data]

    for i, (val, random_index) in enumerate(data):
        if i + 1 < len(data):
            nodes[i].next = nodes[i + 1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]
    return nodes[0]


def main():

    solution = Solution()

    head = [[3, None], [7, 3], [4, 0], [5, 1]]
    head_ll = createLinkedList(head)
    print(f"The reversed linked list is {listToArr(solution.copyRandomList(head_ll))}")

    head = [[1, None], [2, 2], [3, 2]]
    head_ll = createLinkedList(head)
    print(f"The reversed linked list is {listToArr(solution.copyRandomList(head_ll))}")

    return None


if __name__ == "__main__":
    main()

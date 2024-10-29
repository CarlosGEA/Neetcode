"""
Difficulty : Medium
Date created : 29-10-2024
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

        copyNodes = {None: None}
        dummy = head
        while dummy:
            copyNodes[dummy] = Node(dummy.val)
            dummy = dummy.next

        newNode = Node(0)

        dummy = head
        while dummy:
            newNode.next = copyNodes[dummy]
            newNode = newNode.next
            newNode.random = copyNodes[dummy.random]
            dummy = dummy.next

        return copyNodes[head]


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

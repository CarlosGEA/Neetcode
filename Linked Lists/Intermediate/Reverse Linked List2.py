"""
Difficulty : Easy
Date created : 31-10-2024
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        prev = None
        while head:
            next_node = head.next
            head.next = prev

            prev = head
            head = next_node

        return prev



def arrayToList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def printLinkedList(head):
    current = head
    arr = []
    while current:
        arr.append(current.val)
        current = current.next
    return arr


def main():

    solution = Solution()

    head = [0, 1, 2, 3]
    head_ll = arrayToList(head)
    print(f"The reversed linked list is {printLinkedList(solution.reverseList(head_ll))}")

    head = []
    head_ll = arrayToList(head)
    print(f"The reversed linked list is {printLinkedList(solution.reverseList(head_ll))}")

    return None


if __name__ == "__main__":
    main()

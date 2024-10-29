"""
Difficulty : Medium
Date created : 29-10-2024
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        dummy = prev = ListNode()
        prev.next = head

        # while n - 1:
        while n:
            head = head.next
            n -= 1

        # while head.next:
        while head:
            head = head.next
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next


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

    head = [1, 2, 3, 4]
    n = 2
    head_ll = arrayToList(head)
    print(f"The new list is {printLinkedList(solution.removeNthFromEnd(head_ll, n))}")

    head = [5]
    n = 1
    head_ll = arrayToList(head)
    print(f"The new linked list is {printLinkedList(solution.removeNthFromEnd(head_ll, n))}")

    head = [1, 2]
    n = 2
    head_ll = arrayToList(head)
    print(f"The new linked list is {printLinkedList(solution.removeNthFromEnd(head_ll, n))}")

    return None


if __name__ == "__main__":
    main()

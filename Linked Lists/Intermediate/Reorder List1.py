"""
Difficulty : Medium
Date created : 29-10-2024
"""

def listToArr(head):
    current = head
    arr = []
    while current:
        arr.append(current.val)
        current = current.next
    return arr


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reorderList(self, head: ListNode | None) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node

        node = dummy = ListNode()
        while head.next:
            node.next = head
            head = head.next
            node = node.next
            node.next = prev
            prev = prev.next
            node = node.next


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


def main():

    solution = Solution()

    head = [2, 4, 6, 8]
    head_ll = arrayToList(head)
    print(f"The reversed linked list is {(listToArr(solution.reorderList(head_ll)))}")

    head = [2, 4, 6, 8, 10]
    head_ll = arrayToList(head)
    print(f"The reversed linked list is {(listToArr(solution.reorderList(head_ll)))}")

    return None


if __name__ == "__main__":
    main()

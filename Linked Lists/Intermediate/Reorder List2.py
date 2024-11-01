"""
Difficulty : Medium
Date created : 01-11-2024
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
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        dummy = slow.next
        prev = slow.next = None
        while dummy:
            next_node = dummy.next
            dummy.next = prev

            prev = dummy
            dummy = next_node

        dummy = head
        while prev:
            tmp1 = head.next
            tmp2 = prev.next

            head.next = prev
            prev.next = tmp1

            head = tmp1
            prev = tmp2

        head = dummy

        return dummy


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

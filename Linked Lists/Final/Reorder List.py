"""
Difficulty : Medium
Date created : 19-11-2024
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
            slow = slow = slow.next
            fast = fast.next.next


        prev = None
        rev_list = slow.next
        slow.next = None

        while rev_list:
            tmp = rev_list.next
            rev_list.next = prev
            prev = rev_list
            rev_list = tmp

        l1 = head
        l2 = prev
        while l2:
            tmp1 = l1.next
            tmp2 = l2.next

            l1.next = l2
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2

        return head


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
    print(f"The reversed linked list is {print(listToArr(solution.reorderList(head_ll)))}")

    head = [2, 4, 6, 8, 10]
    head_ll = arrayToList(head)
    print(f"The reversed linked list is {print(listToArr(solution.reorderList(head_ll)))}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 25-10-2024
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
        
        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp


        second = prev #  New head of second half of the list
        first = head

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

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

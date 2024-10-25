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

    def reverseList(self, head: ListNode | None) -> ListNode | None:

        curr = head
        prev = None

        while curr is not None:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node

        return prev
    

    def reorderList(self, head: ListNode | None) -> None:
        reversed = self.reverseList(head)

        print(listToArr(head))
        print(listToArr(reversed))

        dummy = start = ListNode()
        # i = 0
        # while head.val != reversed.next.val and reversed.val != head.next.val:
        #     if i % 2 == 0:
        #         dummy.next = head
        #         head = head.next

        #     else:
        #         dummy.next = reversed
        #         reversed = reversed.next

        return start


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

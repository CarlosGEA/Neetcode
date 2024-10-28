"""
Difficulty : Easy
Date created : 25-10-2024
"""


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


def arrayToList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def listToArr(head):
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
    print(f"The reversed linked list is {listToArr(solution.reverseList(head_ll))}")

    head = []
    head_ll = arrayToList(head)
    print(f"The reversed linked list is {listToArr(solution.reverseList(head_ll))}")

    return None


if __name__ == "__main__":
    main()

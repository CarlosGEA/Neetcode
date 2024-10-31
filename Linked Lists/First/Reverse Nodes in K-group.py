"""
Difficulty : Hard
Date created : 31-10-2024
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:

        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next

        curr = head
        prev = None

        old_tail = dummy = ListNode
        new_tail = head
        while length >= k:

            prev = None
            sublength = 0
            while sublength < k:
                # while curr is not None:
                next_node = curr.next
                curr.next = prev

                prev = curr
                curr = next_node
                sublength += 1

            old_tail.next = prev
            old_tail = new_tail
            new_tail = curr
            length -= k

        if length > 0:
            old_tail.next = curr

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


def listToArr(head):
    current = head
    arr = []
    while current:
        arr.append(current.val)
        current = current.next
    return arr


def main():

    solution = Solution()

    head = [1, 2, 3, 4, 5, 6]
    k = 3
    head_ll = arrayToList(head)
    print(f"The reversed linked list is {listToArr(solution.reverseKGroup(head_ll, k))}")

    head = [1, 2, 3, 4, 5]
    k = 3
    head_ll = arrayToList(head)
    print(f"The reversed linked list is {listToArr(solution.reverseKGroup(head_ll, k))}")

    return None


if __name__ == "__main__":
    main()

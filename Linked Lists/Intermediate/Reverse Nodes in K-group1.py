"""
Difficulty : Hard
Date created : 03-11-2024
New Attempt : 06-11-2024
New Attempt : 09-11-2024
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:

        prevGroup = dummy = ListNode(0, head)

        while True:

            kth = self.getKth(prevGroup, k)
            if not kth:
                break

            nextGroup = kth.next

            prev = prevGroup
            cur = prevGroup.next

            while cur != nextGroup:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp
            prevGroup.next = nextGroup

        return dummy.next

    def getKth(self, cur, k):
        while cur and k:
            cur = cur.next
            k -= 1

        return cur


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

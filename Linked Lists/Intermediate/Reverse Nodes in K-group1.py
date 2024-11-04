"""
Difficulty : Hard
Date created : 03-11-2024
Date completed :
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:

        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:

            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next           
            while curr != groupNext:
                next_node = curr.next
                curr.next = prev

                prev = curr
                curr = next_node

            next_node = groupPrev.next
            groupPrev.next = kth
            groupPrev = next_node

        return dummy.next
    
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


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

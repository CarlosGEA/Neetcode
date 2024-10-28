"""
Difficulty : Medium
Date created : 28-10-2024
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next


        return False


def arrayToList(arr, index):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for idx, value in enumerate(arr):

        if index == idx:
            cycle = current
        
        if idx == 0:
            continue

        current.next = ListNode(value)
        current = current.next

       
    if index != -1:
        current.next = cycle
        
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

    head = [1,2,3,4]
    index = 1
    head_ll = arrayToList(head, index)
    print(f"This list has a cycle : {solution.hasCycle(head_ll)}")

    head = [1,2]
    index = -1
    head_ll = arrayToList(head, index)
    print(f"This list has a cycle : {solution.hasCycle(head_ll)}")


    return None


if __name__ == "__main__":
    main()

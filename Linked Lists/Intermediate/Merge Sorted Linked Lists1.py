"""
Difficulty : Easy
Date created : 28-10-2024
"""


def printLinkedList(head):
    current = head
    arr = []
    while current:
        arr.append(current.val)
        current = current.next
    return arr


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        dummy = newlist = ListNode()

        while list1 or list2:

            val1 = list1.val if list1 else float("inf")
            val2 = list2.val if list2 else float("inf")
            if val1 > val2:
                newlist.next = list2
                list2 = list2.next
            else:
                newlist.next = list1
                list1 = list1.next


            newlist = newlist.next

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

    list1 = [1, 2, 4]
    list2 = [1, 3, 5]
    print(
        f"The head of the sorted linked list is {printLinkedList(solution.mergeTwoLists(arrayToList(list1), arrayToList(list2)))}"
    )

    list1 = []
    list2 = [1, 2]
    print(
        f"The head of the sorted linked list is {printLinkedList(solution.mergeTwoLists(arrayToList(list1), arrayToList(list2)))}"
    )

    list1 = []
    list2 = []
    print(
        f"The head of the sorted linked list is {printLinkedList(solution.mergeTwoLists(arrayToList(list1), arrayToList(list2)))}"
    )

    list1 = [-10, -9, -6, -4, 1, 9, 9]
    list2 = [-5, -3, 0, 7, 8, 8]
    print(
        f"The head of the sorted linked list is {printLinkedList(solution.mergeTwoLists(arrayToList(list1), arrayToList(list2)))}"
    )

    return None


if __name__ == "__main__":
    main()

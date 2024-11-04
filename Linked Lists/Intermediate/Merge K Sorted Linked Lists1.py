"""
Difficulty : Hard
Date created : 31-10-2024
"""


def listToArr(head):
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
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        if not lists:
            return None

        while len(lists) > 1:
            newlists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                # newlists.append(listToArr(self.mergeTwoLists(arrayToList(l1), arrayToList(l2))))
                newlists.append(self.mergeTwoLists(l1, l2))

            lists = newlists
        return lists[0]

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

    lists = [[1, 2, 4], [1, 3, 5], [3, 6]]
    print(f"The head of the sorted linked list is {solution.mergeKLists(lists)}")

    lists = []
    print(f"The head of the sorted linked list is {solution.mergeKLists(lists)}")

    lists = [[1, 2, 4]]
    print(f"The head of the sorted linked list is {solution.mergeKLists(lists)}")

    lists = [[-4, -2, 1, 3, 5], [-1, 24, 25], [7], [8], [7], [6], [-7], [-8], [-7], [-6]]
    print(f"The head of the sorted linked list is {solution.mergeKLists(lists)}")

    return None


if __name__ == "__main__":
    main()

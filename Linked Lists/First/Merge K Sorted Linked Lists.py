"""
Difficulty : Hard
Date created : 31-10-2024
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
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        if len(lists) == 0:
            return None

        elif len(lists) == 1:
            return arrayToList(lists[0])
            # return lists[0]

        list1 = arrayToList(lists[0])
        # list1 = res = lists[0]

        for list2 in lists[1:]:
            list2 = arrayToList(list2)  # remove
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
            list1 = dummy.next

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

    # lists = [[1, 2, 4], [1, 3, 5], [3, 6]]
    # print(f"The head of the sorted linked list is {printLinkedList(solution.mergeKLists(lists))}")

    # lists = []
    # print(f"The head of the sorted linked list is {printLinkedList(solution.mergeKLists(lists))}")

    # lists = [[1, 2, 4]]
    # print(f"The head of the sorted linked list is {printLinkedList(solution.mergeKLists(lists))}")

    lists = [[-4, -2, 1, 3, 5], [-1, 24, 25], [7], [8], [7], [6], [-7], [-8], [-7], [-6]]
    print(f"The head of the sorted linked list is {printLinkedList(solution.mergeKLists(lists))}")

    return None


if __name__ == "__main__":
    main()

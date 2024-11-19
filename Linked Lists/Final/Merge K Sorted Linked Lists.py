"""
Difficulty : Hard
Date created : 19-11-2024
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        if not lists:
            return None

        while len(lists) > 1:

            new_list = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                # new_list.append(self.mergeLists(l1, l2))
                new_list.append(listToArr(self.mergeLists(arrayToList(l1), arrayToList(l2))))

            lists = new_list

        return lists[0]

    def mergeLists(self, l1, l2) -> ListNode:

        dummy = head = ListNode()

        while l1 and l2:

            val1 = l1.val
            val2 = l2.val

            if val2 > val1:
                head.next = l1
                l1 = l1.next

            else:
                head.next = l2
                l2 = l2.next

            head = head.next

        head.next = l1 or l2

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

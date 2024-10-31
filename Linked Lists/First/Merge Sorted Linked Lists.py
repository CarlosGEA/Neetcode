"""
Difficulty : Easy
Date created : 25-10-2024
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
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        

        if list1.val > list2.val:
            temp = list2
            list2 = list1
            list1 = temp

        curr1 = list1
        curr2 = list2
        head = curr1

        while curr1.next is not None and curr2 is not None:
            if curr1.next.val > curr2.val:
                temp = curr1.next
                curr1.next = curr2
                curr2 = curr2.next
                curr1.next.next = temp
                curr1 = curr1.next
            else:
                curr1 = curr1.next
            # print(listToArr(curr1))
            # print(listToArr(curr2))

        if curr2 is not None:
            curr1.next = curr2

        return head


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

    # list1 = [1, 2, 4]
    # list2 = [1, 3, 5]
    # print(
    #     f"The head of the sorted linked list is {listToArr(solution.mergeTwoLists(arrayToList(list1), arrayToList(list2)))}"
    # )

    # list1 = []
    # list2 = [1, 2]
    # print(
    #     f"The head of the sorted linked list is {listToArr(solution.mergeTwoLists(arrayToList(list1), arrayToList(list2)))}"
    # )

    # list1 = []
    # list2 = []
    # print(
    #     f"The head of the sorted linked list is {listToArr(solution.mergeTwoLists(arrayToList(list1), arrayToList(list2)))}"
    # )

    list1=[-10,-9,-6,-4,1,9,9]
    list2=[-5,-3,0,7,8,8]
    print(
        f"The head of the sorted linked list is {listToArr(solution.mergeTwoLists(arrayToList(list1), arrayToList(list2)))}"
    )


    return None


if __name__ == "__main__":
    main()

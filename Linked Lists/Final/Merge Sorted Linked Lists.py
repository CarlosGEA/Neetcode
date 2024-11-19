"""
Difficulty : Easy
Date created : 19-11-2024
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
        
        new_head = dummy = ListNode()
        
        while list1 and list2:

            l1 = list1.val 
            l2 = list2.val 

            if l2 > l1:
                new_head.next = list1
                list1 = list1.next

            else:
                new_head.next = list2
                list2 = list2.next

            new_head = new_head.next

        if list1:
            new_head.next = list1
        else:
            new_head.next = list2

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

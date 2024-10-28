"""
Difficulty : Medium
Date created : -10-2024
"""
# change dateeeee

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


class Solution:

    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        return

def main():

    solution = Solution()

    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    print(
        f"The sum of l1 and l2 is {listToArr(solution.addTwoNumbers(arrayToList(l1), arrayToList(l2)))}"
    )

    l1 = [9]
    l2 = [9]
    print(
        f"The sum of l1 and l2 is {listToArr(solution.addTwoNumbers(arrayToList(l1), arrayToList(l2)))}"
    )

    l1=[9,9,9,9,9,9,9]
    l2=[9,9,9,9]
    print(
        f"The sum of l1 and l2 is {listToArr(solution.addTwoNumbers(arrayToList(l1), arrayToList(l2)))}"
    )

    return None


if __name__ == "__main__":
    main()

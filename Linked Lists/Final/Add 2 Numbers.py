"""
Difficulty : Medium
Date created : 19-11-2024
"""


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

        head = dummy = ListNode()
        remainder = 0
        while l1 or l2 or remainder:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sumval = val1 + val2 + remainder
            remainder = sumval // 10
            sumval = sumval % 10

            head.next = ListNode(sumval)

            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


def main():

    solution = Solution()

    # l1 = [1, 2, 3]
    # l2 = [4, 5, 6]
    # print(
    #     f"The sum of l1 and l2 is {listToArr(solution.addTwoNumbers(arrayToList(l1), arrayToList(l2)))}"
    # )

    # l1 = [9]
    # l2 = [9]
    # print(
    #     f"The sum of l1 and l2 is {listToArr(solution.addTwoNumbers(arrayToList(l1), arrayToList(l2)))}"
    # )

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    print(
        f"The sum of l1 and l2 is {listToArr(solution.addTwoNumbers(arrayToList(l1), arrayToList(l2)))}"
    )

    return None


if __name__ == "__main__":
    main()

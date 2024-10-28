"""
Difficulty : Medium
Date created : 27-10-2024
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

        head = ListNode()
        dummy = head

        while l2 or l1:
            val1 = val2 = remainder = 0
            if l1 is not None:
                val1 = l1.val
                l1 = l1.next

            if l2 is not None:
                val2 = l2.val
                l2 = l2.next

            valsum = val1 + val2 + head.val

            if valsum >= 10:
                remainder = 1

            valsum = valsum % 10

            head.val = valsum
            if l1 is not None or l2 is not None:
                head.next = ListNode(remainder)
                head = head.next

        if remainder > 0:
            head.next = ListNode(remainder)
        return dummy


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

    l1=[9,9,9,9,9,9,9]
    l2=[9,9,9,9]
    print(
        f"The sum of l1 and l2 is {listToArr(solution.addTwoNumbers(arrayToList(l1), arrayToList(l2)))}"
    )

    return None


if __name__ == "__main__":
    main()

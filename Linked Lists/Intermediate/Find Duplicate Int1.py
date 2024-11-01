"""
Difficulty : Medium
Date created : 29-10-2024
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        nodes = [ListNode(i) for i in range(len(nums))]
        for i, node in enumerate(nodes):
            node.next = nodes[nums[i]]

        slow = fast = nodes[0]

        while True:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        slow2 = nodes[0]
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next

        return slow.val


def main():

    solution = Solution()

    nums = [1, 2, 3, 2, 2]
    print(f"The duplicate element is {solution.findDuplicate(nums)}")

    nums = [1, 2, 3, 4, 4]
    print(f"The duplicate element is {solution.findDuplicate(nums)}")

    return None


if __name__ == "__main__":
    main()

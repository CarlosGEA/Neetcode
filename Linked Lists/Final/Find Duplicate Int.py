"""
Difficulty : Medium
Date created : 19-11-2024
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow1 = slow
        slow2 = 0
        while True:
            if slow1 == slow2:
                return slow1

            slow1 = nums[slow1]
            slow2 = nums[slow2]


def main():

    solution = Solution()

    nums = [1, 2, 3, 2, 2]
    print(f"The duplicate element is {solution.findDuplicate(nums)}")

    nums = [1, 2, 3, 4, 4]
    print(f"The duplicate element is {solution.findDuplicate(nums)}")

    return None


if __name__ == "__main__":
    main()

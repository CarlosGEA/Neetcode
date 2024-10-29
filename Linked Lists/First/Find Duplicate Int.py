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

        head = ListNode()
        dummy = head
        for n in nums:
            
            check = head
            while check:
                if n == check.val:
                    return n
                check = check.next
            
            dummy.next = ListNode(n)
            dummy = dummy.next



        # seen = set()

        # for n in nums:
        #     if n in seen:
        #         return n
        #     seen.add(n)

        return None



def main():

    solution = Solution()

    nums = [1,2,3,2,2]
    print(f"The duplicate element is {solution.findDuplicate(nums)}")

    nums = [1,2,3,4,4]
    print(f"The duplicate element is {solution.findDuplicate(nums)}")
   
    return None


if __name__ == "__main__":
    main()
"""
Difficulty : Easy
Date created : 04-11-2024
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        height_diff = []

        def getHeights(node):

            if not node:
                return 0

            lh = 1 + getHeights(node.left)
            rh = 1 + getHeights(node.right)
            height_diff.append(abs(lh - rh))

            return max(lh, rh)

        getHeights(root)
        for h in height_diff:
            if h > 1:
                return False
        return True


def arrToTree(arr):
    if not arr:
        return None

    nodes = []

    val = arr.pop(0)
    root = TreeNode(val)
    nodes.append(root)

    while len(arr) > 0:
        curr = nodes.pop(0)

        left_val = arr.pop(0)
        if left_val is not None:
            curr.left = TreeNode(left_val)
            nodes.append(curr.left)

        if len(arr) > 0:
            right_val = arr.pop(0)
            if right_val is not None:
                curr.right = TreeNode(right_val)
                nodes.append(curr.right)

    return root


def treeToArr(root):

    arr = []
    stack = [root]

    while stack:
        node = stack.pop(0)
        if node:
            arr.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        else:
            arr.append(None)

    while arr and arr[-1] is None:
        arr.pop()

    return arr


def main():

    solution = Solution()

    root = [1, 2, 3, None, None, 4, None, 5]
    print(f"The binary tree is balanced? : {solution.isBalanced(arrToTree(root))}")

    root = [1, 2, 3, None, None, 4]
    print(f"The binary tree is balanced? : {solution.isBalanced(arrToTree(root))}")

    root = []
    print(f"The binary tree is balanced? : {solution.isBalanced(arrToTree(root))}")

    return None


if __name__ == "__main__":
    main()

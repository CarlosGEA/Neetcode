"""
Difficulty : Easy 
Date created : 19-12-2024
New attempt : 08-01-2025
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            maxL = dfs(node.left)
            maxR = dfs(node.right)

            res = max(res, max(maxL, maxR), maxL + maxR)

            return 1 + max(maxL, maxR)

        dfs(root)
        return res
    

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

    root = [1, None, 2, 3, 4, 5]
    print(f"The diameter of the binary tree is {solution.diameterOfBinaryTree(arrToTree(root))}")

    root = [1, 2, 3]
    print(f"The diameter of the binary tree is {solution.diameterOfBinaryTree(arrToTree(root))}")

    root = [1, 4, 3, 2]
    print(f"The diameter of the binary tree is {solution.diameterOfBinaryTree(arrToTree(root))}")

    return None


if __name__ == "__main__":
    main()

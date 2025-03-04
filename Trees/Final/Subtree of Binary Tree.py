"""
Difficulty : Easy
Date created : 19-12-2024
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        if not root:
            return False

        if not subRoot:
            return True

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, p, q):

        if not p and not q:
            return True

        elif not p or not q:
            return False

        else:
            return (
                p.val == q.val and self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
            )


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

    root = [1, 2, 3, 4, 5]
    subRoot = [2, 4, 5]
    print(
        f"Is the subRoot actually a subRoot of root? : {solution.isSubtree(arrToTree(root), arrToTree(subRoot))}"
    )

    root = [1, 2, 3, 4, 5, None, None, 6]
    subRoot = [2, 4, 5]
    print(
        f"Is the subRoot actually a subRoot of root? : {solution.isSubtree(arrToTree(root), arrToTree(subRoot))}"
    )

    root = [1, 1]
    subRoot = [1]
    print(
        f"Is the subRoot actually a subRoot of root? : {solution.isSubtree(arrToTree(root), arrToTree(subRoot))}"
    )

    root = [3, 4, 5, 1, None, 2]
    subRoot = [3, 1, 2]
    print(
        f"Is the subRoot actually a subRoot of root? : {solution.isSubtree(arrToTree(root), arrToTree(subRoot))}"
    )

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Easy
Date created : 12-11-2024
New Attempt : 15-11-2024
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not subRoot:
            return True

        if not root:
            return False
        
        if self.isSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, root, subroot) -> bool:

        if not root and not subroot:
            return True

        if not root or not subroot or root.val != subroot.val:
            return False

        return self.isSame(root.left, subroot.left) and self.isSame(root.right, subroot.right)


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
        f"Does subroot exist in root? : {solution.isSubtree(arrToTree(root), arrToTree(subRoot))}"
    )

    root = [1, 2, 3, 4, 5, None, None, 6]
    subRoot = [2, 4, 5]
    print(
        f"Does subroot exist in root? : {solution.isSubtree(arrToTree(root), arrToTree(subRoot))}"
    )

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 13-11-2024
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def dfs(node, l, r):
            if not node:
                return True

            if not l < node.val < r:
                return False

            return dfs(node.left, l, node.val) and dfs(node.right, node.val, r)

        return dfs(root, float("-inf"), float("inf"))


def main():

    solution = Solution()

    root = [2, 1, 3]
    print(f"This is a valid binary search tree? : {solution.isValidBST(arrToTree(root))}")

    root = [1, 2, 3]
    print(f"This is a valid binary search tree? : {solution.isValidBST(arrToTree(root))}")

    root = [5, 4, 6, None, None, 3, 7]
    print(f"This is a valid binary search tree? : {solution.isValidBST(arrToTree(root))}")

    return None


if __name__ == "__main__":
    main()

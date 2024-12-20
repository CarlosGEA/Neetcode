"""
Difficulty : Medium
Date created : 20-12-2024
New attempt : 23-12-2024
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
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        arr = []
        stack = [root]

        while stack:
            node = stack.pop(0)
            if node:
                arr.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return sorted(arr)[k - 1]


def main():

    solution = Solution()

    root = [2, 1, 3]
    k = 1
    print(f"The {k}th smallest element in the tree is {solution.kthSmallest(arrToTree(root), k)}")

    root = [4, 3, 5, 2, None]
    k = 4
    print(f"The {k}th smallest element in the tree is {solution.kthSmallest(arrToTree(root), k)}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Hard
Date created : -11-2024
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumPath(self, root: TreeNode | None) -> int:

        return


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

    root = [1, 2, 3]
    print(f"The maximum sum path in this tree is {solution.maxSumPath(arrToTree(root))}")

    root = [-15, 10, 20, None, None, 15, 5, -5]
    print(f"The maximum sum path in this tree is {solution.maxSumPath(arrToTree(root))}")

    return None


if __name__ == "__main__":
    main()

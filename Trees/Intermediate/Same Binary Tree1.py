"""
Difficulty : Easy
Date created : 08-11-2024
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        if not p and not q:
            return True
        if not p or not q:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val


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

    p = [1, 2, 3]
    q = [1, 2, 3]
    print(f"p and q the same binary tree? : {solution.isSameTree(arrToTree(p), arrToTree(q))}")

    p = [4, 7]
    q = [4, None, 7]
    print(f"p and q the same binary tree? : {solution.isSameTree(arrToTree(p), arrToTree(q))}")

    p = [1, 2, 3]
    q = [1, 3, 2]
    print(f"p and q the same binary tree? : {solution.isSameTree(arrToTree(p), arrToTree(q))}")

    return None


if __name__ == "__main__":
    main()

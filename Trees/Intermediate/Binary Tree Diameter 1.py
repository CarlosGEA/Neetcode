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
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        self.max_depth = 0

        def dfs(node):
            if not node:
                return 0

            ld = dfs(node.left)
            rd = dfs(node.right)
            self.max_depth = max(self.max_depth, ld + rd)
            return max(ld, rd) + 1

        dfs(root)
        return self.max_depth


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
    print(f"The diameter of the tree is {solution.diameterOfBinaryTree(arrToTree(root))}")

    root = [1, 2, 3]
    print(f"The diameter of the tree is {solution.diameterOfBinaryTree(arrToTree(root))}")

    return None


if __name__ == "__main__":
    main()

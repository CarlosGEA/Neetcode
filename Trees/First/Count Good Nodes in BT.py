"""
Difficulty : Medium
Date created : 06-11-2024
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
    def goodNodes(self, root: TreeNode) -> int:

        count = 0

        def dfs(node, maxval):

            nonlocal count

            if not node:
                return

            if node.val >= maxval:
                count += 1

            if node.left:
                dfs(node.left, max(node.left.val, maxval))
            if node.right:
                dfs(node.right, max(node.right.val, maxval))

            return

        dfs(root, root.val)

        return count


def main():

    solution = Solution()

    # root = [2, 1, 1, 3, None, 1, 5]
    root = [3, 3, None, 4, 2]
    print(f"The number of good nodes in this tree is {solution.goodNodes(arrToTree(root))}")

    root = [1, 2, -1, 3, 4]
    print(f"The number of good nodes in this tree is {solution.goodNodes(arrToTree(root))}")

    return None


if __name__ == "__main__":
    main()

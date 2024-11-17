"""
Difficulty : Medium
Date created : 09-11-2024
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, maxval):
            # go through each node, checking previous path, max value and adding 1 if it's less than or equal, use dfs or stack ??

            if not node:
                return
            
            nonlocal res
            if node.val >= maxval:
                maxval = node.val
                res += 1
            dfs(node.left, maxval)
            dfs(node.right, maxval)

            return None

        dfs(root, float("-inf"))

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

    root = [2, 1, 1, 3, None, 1, 5]
    print(f"The number of good nodes in the tree is {solution.goodNodes(arrToTree(root))}")

    root = [1, 2, -1, 3, 4]
    print(f"The number of good nodes in the tree is {solution.goodNodes(arrToTree(root))}")

    return None


if __name__ == "__main__":
    main()

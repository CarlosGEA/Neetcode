"""
Difficulty : Hard
Date created : 21-11-2024
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:

        res = float("-inf")

        def dfs(node):
            if not node:
                return 0

            cur = node.val

            left_val = dfs(node.left)
            right_val = dfs(node.right)

            nonlocal res
            res = max(res, cur + left_val + right_val)

            return max(0, cur, cur + max(left_val, right_val))

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

    root = [-15, 10, 20, None, None, 15, 5, -5]
    print(f"The max sum path of the tree is {solution.maxPathSum(arrToTree(root))}")

    root = [1, 2, 3]
    print(f"The max sum path of the tree is {solution.maxPathSum(arrToTree(root))}")

    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    print(f"The max sum path of the tree is {solution.maxPathSum(arrToTree(root))}")

    return None


if __name__ == "__main__":
    main()

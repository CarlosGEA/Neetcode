"""
Difficulty : Medium
Date created : 21-11-2024
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        # same as before, recursive but now have other function, working through left, right
        # store and increment value of the preorder index and indices for inorder so look up
        if not preorder:
            return None

        mid = preorder[0]
        split = inorder.index(mid)

        root = TreeNode(mid)
        root.left = self.buildTree(preorder[1 : split + 1], inorder[:split])
        root.right = self.buildTree(preorder[split + 1 :], inorder[split + 1 :])

        return root



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

    preorder = [1, 2, 3, 4]
    inorder = [2, 1, 3, 4]
    print(f"The tree built is {treeToArr(solution.buildTree(preorder, inorder))}")

    preorder = [1]
    inorder = [1]
    print(f"The tree built is {treeToArr(solution.buildTree(preorder, inorder))}")

    return None


if __name__ == "__main__":
    main()

"""
Difficulty : Medium
Date created : 08-11-2024
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pval = p#.val
        qval = q#.val


        while root:              

            if (pval <= root.val and qval >= root.val) or (pval >= root.val and qval <= root.val):
                return root
                
            
            elif pval <= root.val and qval <= root.val:
                root = root.left
            else:
                root = root.right


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

    root = [5, 3, 8, 1, 4, 7, 9, None, 2]
    p = 3
    q = 8
    print(
        f"The lowest common ancester of {p} and {q} is {solution.lowestCommonAncestor(arrToTree(root), p, q)}"
    )

    root = [5, 3, 8, 1, 4, 7, 9, None, 2]
    p = 3
    q = 4
    print(
        f"The lowest common ancester of {p} and {q} is {solution.lowestCommonAncestor(arrToTree(root), p, q)}"
    )

    return None


if __name__ == "__main__":
    main()

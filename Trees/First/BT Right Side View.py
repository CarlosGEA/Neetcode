"""
Difficulty : Medium
Date created : 06-11-2024
"""

from collections import deque


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
    def rightSideView(self, root: TreeNode | None) -> list[int]:

        if not root:
            return []

        stack = deque([root])
        res = []
        while stack:

            res.append(stack[0].val)

            level = deque()

            for _ in range(len(stack)):
                node = stack.popleft()

                if node.right:
                    level.append(node.right)
                if node.left:
                    level.append(node.left)

            stack = deque(level)

        return res


def main():

    solution = Solution()

    # root = [1, 2, 3]
    # print(
    #     f"The value of the nodes only visible from the right are {solution.rightSideView(arrToTree(root))}"
    # )

    # root = [1, 2, 3, 4, 5, 6, 7]
    # print(
    #     f"The value of the nodes only visible from the right are {solution.rightSideView(arrToTree(root))}"
    # )

    root = [4, 3, 6, 1, None, 5, None, None, 2]
    print(
        f"The value of the nodes only visible from the right are {solution.rightSideView(arrToTree(root))}"
    )
    return None


if __name__ == "__main__":
    main()

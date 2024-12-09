"""
Difficulty : 
Date created : 03-12-2024
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root: TreeNode | None) -> str:

        arr = []
        stack = [root]

        while stack:
            node = stack.pop(0)
            if node:
                arr.append(str(node.val))
                stack.append(node.left)
                stack.append(node.right)
            else:
                arr.append("?")

        while arr and arr[-1] == "?":
            arr.pop()

        arr = "#".join(arr)

        return arr

    def deserialize(self, data: str) -> TreeNode | None:
        if not data:
            return None

        nodes = []
        arr = data.split("#")

        val = arr.pop(0)
        root = TreeNode(int(val))
        nodes.append(root)

        while len(arr) > 0:
            curr = nodes.pop(0)

            left_val = arr.pop(0)
            if left_val != "?":
                curr.left = TreeNode(int(left_val))
                nodes.append(curr.left)

            if len(arr) > 0:
                right_val = arr.pop(0)
                if right_val != "?":
                    curr.right = TreeNode(int(right_val))
                    nodes.append(curr.right)

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

    decode = Codec()
    root = [1, 2, 3, None, None, 4, 5]
    serialized = decode.serialize(arrToTree(root))
    print(f"The serialized tree is :{serialized}")
    print(f"The deserialized tree is {treeToArr(decode.deserialize(serialized))}")

    root = []
    serialized = decode.serialize(arrToTree(root))
    print(f"The serialized tree is :{serialized}")
    print(f"The deserialized tree is {treeToArr(decode.deserialize(serialized))}")

    return None


if __name__ == "__main__":
    main()
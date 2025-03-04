"""
Difficulty : Hard
Date created : 13-12-2024
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root: TreeNode | None) -> str:
        serialized = []

        def dfs(node):
            if not node:
                serialized.append("?")
                return
            serialized.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

            return
        
        dfs(root)
        return "#".join(serialized)

    def deserialize(self, data: str) -> TreeNode | None:
        
        values = data.split("#")
        i = 0
        def dfs():
            nonlocal i
            if values[i] == "?":
                i += 1
                return None
            
            root = TreeNode(int(values[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()


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
    print(f"The serialized tree is : {serialized}")
    print(f"The deserialized tree is {treeToArr(decode.deserialize(serialized))}")

    root = []
    serialized = decode.serialize(arrToTree(root))
    print(f"The serialized tree is : {serialized}")
    print(f"The deserialized tree is {treeToArr(decode.deserialize(serialized))}")

    return None


if __name__ == "__main__":
    main()

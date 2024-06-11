# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode | None) -> str:
        ans = []

        def encode(node: TreeNode | None):
            if not node:
                ans.append('')
                return
            ans.append(str(node.val))
            encode(node.left)
            encode(node.right)

        encode(root)
        return ','.join(ans)

    def deserialize(self, data: str) -> TreeNode | None:
        i = 0

        def decode() -> TreeNode | None:
            nonlocal i
            if i == len(data) or data[i] == ',':
                i += 1
                return None
            j = data.index(',', i)
            node = TreeNode(int(data[i:j]))
            i = j + 1
            node.left = decode()
            node.right = decode()
            return node

        return decode()

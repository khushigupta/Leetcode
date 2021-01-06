# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        serialize_string = self.convert(root)
        return serialize_string

    def convert(self, root):
        if root is None:
            return 'none'
        else:
            return str(root.val) + ',' + self.convert(root.left) + ',' + self.convert(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        return self.convert_tree(data)

    def convert_tree(self, data):
        val = data.pop(0)
        if val == 'none':
            return None

        left = self.convert_tree(data)
        right = self.convert_tree(data)
        root = TreeNode(int(val))

        root.left = left
        root.right = right
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
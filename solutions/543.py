# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None or root.left is None and root.right is None:
            return 0

        d, h = self.diam(root)
        return d

    def diam(self, root):
        if root is None:
            return 0, 0

        dim_left, height_left = self.diam(root.left)
        dim_right, height_right = self.diam(root.right)

        height = max(height_left, height_right) + 1
        dim_curr = max(dim_left, dim_right, height_left + height_right)
        return dim_curr, height



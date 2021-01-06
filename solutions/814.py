# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        root = self.prune(root)[1]

        if root.left is None and root.right is None and root.val == 0:
            return None
        else:
            return root

    def prune(self, root):
        if root is None:
            return False, None

        left_contains_one, left_tree = self.prune(root.left)
        right_contains_one, right_tree = self.prune(root.right)

        if not left_contains_one:
            root.left = None
        if not right_contains_one:
            root.right = None

        contains = left_contains_one or right_contains_one

        if root.val == 1:
            contains = True or contains
        else:
            contains = False or contains
        return contains, root


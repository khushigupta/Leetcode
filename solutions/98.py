# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root)[2]

    def check(self, root):
        if root is None:
            return -sys.maxint, sys.maxint, True

        max_left = -sys.maxint
        min_left = root.val
        max_right = root.val
        min_right = sys.maxint

        valid = False
        valid_left = True
        valid_right = True

        if root.left:
            max_left, min_left, valid_left = self.check(root.left)
        if root.right:
            max_right, min_right, valid_right = self.check(root.right)

        if max_left < root.val < min_right:
            valid = True

        valid = valid and (valid_left and valid_right)
        return max_right, min_left, valid

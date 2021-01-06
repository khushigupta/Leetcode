# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution(object):

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        return self.minDiff(root)[2]

    def minDiff(self, root):
        # post order solution

        if root.left is None and root.right is None:
            return root.val, root.val, sys.maxint

        min_diff = sys.maxint
        min_diff_left = sys.maxint
        min_diff_right = sys.maxint
        max_right = root.val
        min_left = root.val

        if root.left is not None:
            max_left, min_left, min_diff_left = self.minDiff(root.left)
            min_diff = min(abs(root.val - max_left), min_diff)
        if root.right is not None:
            max_right, min_right, min_diff_right = self.minDiff(root.right)
            min_diff = min(abs(root.val - min_right), min_diff)

        min_diff = min(min_diff_left, min_diff_right, min_diff)

        return max_right, min_left, min_diff


class Solution(object):
    min_dist = sys.maxint
    prev = None

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        self.inorder(root)
        return self.min_dist

    def inorder(self, root):
        # inorder traversal gives us things in sorted order. If this was an array, min diff would be curr - prev,
        # min over everything. but since that's not the case. we need prev, curr in trr
        if root is None:
            return
        self.inorder(root.left)
        if self.prev is not None:
            self.min_dist = min(self.min_dist, root.val - self.prev)
        self.prev = root.val
        self.inorder(root.right)


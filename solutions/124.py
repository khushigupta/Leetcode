# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys


class Solution:
    def maxPathSum(self, root):
        if root is None:
            return 0

        return self.max_sum(root)[1]

    def max_sum(self, root):
        if root is None:
            return -sys.maxint, -sys.maxint

        max_with_root_left, max_so_far_left = self.max_sum(root.left)
        max_with_root_right, max_so_far_right = self.max_sum(root.right)

        max_curr = root.val
        max_curr = max(max_curr, max_curr + max_with_root_left, max_curr + max_with_root_right)

        max_so_far = root.val + max_with_root_left + max_with_root_right
        max_so_far = max(max_so_far_left, max_so_far_right, max_so_far, max_curr)
        return max_curr, max_so_far







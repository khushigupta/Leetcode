# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tilt, sum = self.findLRSum(root)
        return tilt

    def findLRSum(self, root):
        if root is None:
            return 0, 0

        ltilt, left = self.findLRSum(root.left)
        rtilt, right = self.findLRSum(root.right)
        tilt = abs(left - right) + ltilt + rtilt
        sum = left + right + root.val
        return tilt, sum
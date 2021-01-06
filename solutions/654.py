# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return []

        return self.constructTree(nums)

    def constructTree(self, nums):
        if len(nums) == 0:
            return None

        max_idx = -1
        max_val = -sys.maxint
        for i in range(len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
                max_idx = i

        if max_idx == 0:
            left_arr = []
        else:
            left_arr = nums[:max_idx]
        if max_idx == len(nums) - 1:
            right_arr = []
        else:
            right_arr = nums[max_idx + 1:]

        left_tree = self.constructTree(left_arr)
        right_tree = self.constructTree(right_arr)

        root = TreeNode(max_val)
        root.left = left_tree
        root.right = right_tree
        return root



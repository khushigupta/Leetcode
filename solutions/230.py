# https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # in python, lists are stacks
        # let's try inorder traversal

        s = []
        curr = root
        m = 0
        while len(s) != 0 or curr is not None:
            if curr:
                s.append(curr)
                curr = curr.left
            else:
                curr = s.pop()
                m += 1
                if m == k:
                    return curr.val
                curr = curr.right

        return -1
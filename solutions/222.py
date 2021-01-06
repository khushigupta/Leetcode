# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution(object):
    height_dict = defaultdict(TreeNode)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        h = self.height(root)
        num_leaves = self.bin_search(root)
        return num_leaves

    def height(self, root):
        if root is None:
            return 0

        height = max(self.height(root.left), self.height(root.right)) + 1
        self.height_dict[root] = height
        return height

    def bin_search(self, root):
        ans = 1
        temp = root
        while temp:
            if temp.left is None and temp.right is None:
                # found leaf
                break
            if temp.right and self.height_dict[temp.left] == self.height_dict[temp.right]:
                temp = temp.right
                ans = ans * 2 + 1
            else:
                temp = temp.left
                ans = ans * 2
        return ans



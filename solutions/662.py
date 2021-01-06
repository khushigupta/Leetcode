# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/149624/Java-elegant-BFS-solution

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.level_order(root)

    def level_order(self, root):
        max_width = 0
        if root is None:
            return max_width

        q = []
        q.append((root, 1))
        prev_level = 1
        max_width = 1
        level = 1

        while len(q) != 0:
            curr_tuple = q.pop(0)
            node, level = curr_tuple

            if level != prev_level:
                max_width = max(max_width, len(q) + 1)

            if node is None:
                continue

            if node.left is None and node.right is None:
                # don't add if it is a leaf node
                continue

            if node.left:
                q.append((node.left, level + 1))
            else:
                q.append((None, level + 1))

            if node.right:
                q.append((node.right, level + 1))
            else:
                q.append((None, level + 1))

        return max_width
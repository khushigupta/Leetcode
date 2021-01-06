# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        node = self.lca(root, p, q)[2]
        return node

    def lca(self, root, p_node, q_node):
        if root is None:
            return False, False, None

        p_l, q_l, a_l = self.lca(root.left, p_node, q_node)
        p_r, q_r, a_r = self.lca(root.right, p_node, q_node)

        ancestor = None
        p = False
        q = False

        if p_l and q_l:
            ancestor = a_l
        elif p_r and q_r:
            ancestor = a_r

        print(p_node.val)
        if root.val == p_node.val:
            p = True
        if root.val == q_node.val:
            q = True

        p = p or (p_l or p_r)
        q = q or (q_l or q_r)

        if p and q:
            if ancestor is None:
                ancestor = root

        return p, q, ancestor
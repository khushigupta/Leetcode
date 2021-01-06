# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.inorder_list = []
        self.inorder(root)

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        self.inorder_list.append(root.val)
        self.inorder(root.right)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.inorder_list) > 0

    def next(self):
        """
        :rtype: int
        """
        return self.inorder_list.pop(0)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
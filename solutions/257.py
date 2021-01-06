# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []

        return_paths = self.paths2(root)
        string_paths = []
        for path in return_paths:
            path = [str(p) for p in path if p is not None]
            if len(path) == 0:
                continue
            string_paths.append('->'.join(path))
        return string_paths

    def paths(self, root):
        if root is None:
            return []

        new_list = []
        if root.left is None and root.right is None:
            return [[root.val]]

        if root.left is not None:
            left_list = self.paths(root.left)
            for l in left_list:
                new_list.append([root.val] + l)
        if root.right is not None:
            right_list = self.paths(root.right)
            for r in right_list:
                new_list.append([root.val] + r)
        return new_list

    def paths2(self, root):
        if root is None:
            return []

        left_list = self.paths(root.left)
        right_list = self.paths(root.right)

        new_list = []
        if len(left_list) == 0 and len(right_list) == 0:
            return [[root.val]]

        for l in left_list:
            new_list.append([root.val] + l)
        for r in right_list:
            new_list.append([root.val] + r)
        return new_list
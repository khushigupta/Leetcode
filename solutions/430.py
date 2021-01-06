"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        head, _ = self.flat_list(head)
        return head
        a

    def flat_list(self, node):

        start_node = node
        tmp = node
        prev = None

        while tmp:
            prev, next_temp = tmp, tmp.next
            if tmp.child:
                flat_start_node, flat_end_note = self.flat_list(tmp.child)
                tmp.next, flat_start_node.prev = flat_start_node, tmp
                flat_end_note.next = next_temp
                if next_temp:
                    next_temp.prev = flat_end_note
                tmp.child = None
                prev = flat_end_note
            tmp = next_temp
        end_node = prev
        return start_node, end_node



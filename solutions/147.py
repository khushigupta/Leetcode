# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        curr = head.next
        sorted_head = head
        sorted_head.next = None

        while curr:
            # you pick the head node and insert it in the appropriate pos in the new list
            tmp = curr.next
            curr.next = None
            sorted_head = self.insert_node(curr, sorted_head)
            curr = tmp
        return sorted_head

    def insert_node(self, node, sorted_head):

        if node is None:
            return sorted_head

        # insert in beginning
        if sorted_head is None or node.val < sorted_head.val:
            node.next = sorted_head
            return node

        # insert in the middle
        prev, curr = None, sorted_head
        while curr and curr.val <= node.val:
            prev = curr
            curr = curr.next
        prev.next = node
        node.next = curr
        return sorted_head


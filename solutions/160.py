# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        c1 = self.count(headA)
        c2 = self.count(headB)

        # first list is always longer
        if c2 > c1:
            headB, headA = headA, headB
            c1, c2 = c2, c1

        diff = c1 - c2
        tmp1 = headA
        while diff > 0:
            tmp1 = tmp1.next
            diff -= 1

        tmp2 = headB
        while tmp1 and tmp2:
            if tmp1 == tmp2:
                return tmp1
            else:
                tmp1 = tmp1.next
                tmp2 = tmp2.next
        return None

    def count(self, head):
        tmp = head
        count = 0
        while tmp:
            tmp = tmp.next
            count += 1
        return count
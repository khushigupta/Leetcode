# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        N = self.count(head)
        return self.merge_sort(head, N)

        # merge sort

    def count(self, head):
        tmp = head
        count = 0
        while tmp:
            tmp = tmp.next
            count += 1
        return count

    def merge_sort(self, head, N):
        if head is None or head.next is None:
            return head
        right_len = N // 2
        left_len = N - right_len
        prev, tmp, count = None, head, 0

        while count < left_len:
            prev = tmp
            tmp = tmp.next
            count += 1

        left = head
        prev.next = None
        right = tmp

        left_list = self.merge_sort(left, left_len)
        right_list = self.merge_sort(right, right_len)

        return self.merge_list(left_list, right_list)

    def merge_list(self, head1, head2):
        if not head2:
            return head1
        if not head1:
            return head2
        tmp1 = head1
        tmp2 = head2
        head = None
        if tmp1.val < tmp2.val:
            new_head, tmp1 = tmp1, tmp1.next
            head = new_head
        else:
            new_head, tmp2 = tmp2, tmp2.next
            head = new_head
        while tmp1 and tmp2:
            if tmp1.val < tmp2.val:
                new_head.next, tmp1 = tmp1, tmp1.next
            else:
                new_head.next, tmp2 = tmp2, tmp2.next
            new_head = new_head.next
        if tmp1:
            new_head.next = tmp1
        if tmp2:
            new_head.next = tmp2
        return head

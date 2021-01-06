# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        N = self.len_list(head)
        if N == 1:
            return head

        if k >= N:
            k = k % N
        if k == 0:
            return head

        slow_ptr = self.get_new_head(head, k)
        new_head = self.rotate(head, slow_ptr)
        # self.print_list(new_head)
        return new_head

    def len_list(self, head):
        ptr = head
        count = 0
        while ptr:
            ptr = ptr.next
            count += 1
        return count

    def get_new_head(self, head, k):
        ptr = head
        slow_ptr = head
        count = 0

        while ptr and count < k:
            ptr = ptr.next
            count += 1
        while ptr.next:
            slow_ptr = slow_ptr.next
            ptr = ptr.next
        return slow_ptr

    def rotate(self, head, slow_ptr):
        last = slow_ptr
        new_head = slow_ptr.next
        last.next = None
        ptr = new_head
        while ptr.next:
            ptr = ptr.next
        ptr.next = head
        return new_head

    def print_list(self, head):
        ptr = head
        while ptr:
            print(ptr.val)
            ptr = ptr.next





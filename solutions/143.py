# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        N = self.count_nodes(head)
        if N < 3:
            return

        head, mid = self.reverse_second_half(head, N)
        ptr1 = head
        ptr2 = mid.next
        mid.next = None

        count = 0
        while count < N / 2:
            next_ptr1 = ptr1.next
            next_ptr2 = ptr2.next
            ptr1.next = ptr2
            ptr2.next = next_ptr1
            ptr2 = next_ptr2
            ptr1 = next_ptr1
            count += 1

    def count_nodes(self, head):
        count = 0
        tmp = head
        while tmp:
            count += 1
            tmp = tmp.next
        return count

    def reverse_second_half(self, head, count):
        if count < 3:
            return head, None

        tmp = head
        cnt = 0
        while cnt < count / 2 - 1:
            tmp = tmp.next
            cnt += 1
        if count % 2 == 1:
            tmp = tmp.next
            count += 1

        mid = tmp
        first = tmp.next
        second = first.next
        first.next = None

        while second:
            second_next = second.next
            second.next = first
            first = second
            second = second_next
        mid.next = first
        return head, mid




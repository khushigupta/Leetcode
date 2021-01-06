# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head or not head.next:
            return True

        N = self.count_nodes(head)

        # reverse second half of linked list
        head = self.reverse_second_half(head, N)
        ans = self.check_pailndrome(head, N)
        head = self.reverse_second_half(head, N)
        return ans

    def count_nodes(self, head):
        tmp = head
        count = 0
        while tmp:
            tmp = tmp.next
            count += 1
        return count

    def reverse_second_half(self, head, count):

        if count < 3:
            return head

        tmp = head
        cnt = 0
        while cnt < count / 2 - 1:
            tmp = tmp.next
            cnt += 1
        if count % 2 == 1:
            tmp = tmp.next
            cnt += 1
        mid = tmp
        first = mid.next
        second = first.next
        first.next = None
        while second:
            next_second = second.next
            second.next = first
            first = second
            second = next_second
        mid.next = first
        return head

    def print_list(self, head):
        tmp = head
        while tmp:
            print(tmp.val)
            tmp = tmp.next

    def check_pailndrome(self, head, count):
        tmp = head
        cnt = 0
        while cnt < count / 2:
            tmp = tmp.next
            cnt += 1
        if count % 2 == 1:
            tmp = tmp.next
            cnt += 1

        start = head
        mid = tmp
        while mid:
            if start.val != mid.val:
                return False
            mid = mid.next
            start = start.next
        return True









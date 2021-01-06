# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverse_list(l1)
        l2 = self.reverse_list(l2)

        l3 = self.add_list(l1, l2)
        l3 = self.reverse_list(l3)
        return l3

    def reverse_list(self, head):
        if not head or not head.next:
            return head
        first = head
        second = head.next
        first.next = None

        while second:
            second_next = second.next
            second.next = first
            first = second
            second = second_next
        head = first
        return head

    def add_list(self, l1, l2):

        if not l1:
            return l2
        if not l2:
            return l1
        if l1.next is None and l1.val == 0:
            return l2
        if l2.next is None and l2.val == 0:
            return l1

        carry = 0
        tmp1 = l1
        tmp2 = l2

        head = None
        tmp3 = head

        while tmp1 and tmp2:
            new_val = (tmp1.val + tmp2.val + carry) % 10
            carry = (tmp1.val + tmp2.val + carry) // 10
            new_node = ListNode(new_val)
            if not head:
                tmp3 = new_node
                head = new_node
            else:
                tmp3.next = new_node
                tmp3 = tmp3.next
            tmp1 = tmp1.next
            tmp2 = tmp2.next

        while tmp1:
            new_val = (tmp1.val + carry) % 10
            carry = (tmp1.val + carry) // 10
            new_node = ListNode(new_val)
            tmp3.next = new_node
            tmp3 = tmp3.next
            tmp1 = tmp1.next

        while tmp2:
            new_val = (tmp2.val + carry) % 10
            carry = (tmp2.val + carry) // 10
            new_node = ListNode(new_val)
            tmp3.next = new_node
            tmp3 = tmp3.next
            tmp2 = tmp2.next

        if carry != 0:
            new_node = ListNode(carry)
            tmp3.next = new_node

        return head







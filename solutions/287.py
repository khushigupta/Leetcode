class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # this is same as finding entry point of a cycle in a linked list

        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        first = 0
        second = fast
        while first != second:
            first = nums[first]
            second = nums[second]

        return first

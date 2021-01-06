class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        num_zeros = 0
        for n in nums:
            if n == 0:
                num_zeros += 1

        if num_zeros == 0 or num_zeros == len(nums):
            return

        curr_pos = 0
        non_zero_ptr = 0

        while curr_pos < len(nums) - num_zeros:
            if nums[non_zero_ptr] != 0:
                non_zero_ptr += 1
                curr_pos += 1
            else:
                while nums[non_zero_ptr] == 0:
                    non_zero_ptr += 1
                nums[curr_pos], nums[non_zero_ptr] = nums[non_zero_ptr], 0
                curr_pos += 1
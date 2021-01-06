# https://leetcode.com/problems/two-sum/description/


# this is nlog(n) can be solved easily in order(n) using maps
# same solution can be used for 167.py

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []

        my_nums = sorted((e, i) for i, e in enumerate(nums))

        begin = 0
        end = len(nums) - 1

        while (begin < end):
            curr_sum = my_nums[begin][0] + my_nums[end][0]
            if curr_sum > target:
                end = end - 1
            elif curr_sum < target:
                begin = begin + 1
            else:
                break

        if begin != end and my_nums[begin][0] + my_nums[end][0] == target:
            return [my_nums[begin][1], my_nums[end][1]]
        else:
            return []


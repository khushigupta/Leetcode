class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        new_arr_idx = 0
        curr_idx = 0
        prev_element = nums[0]
        ele_count = 0
        length = 0

        while curr_idx < len(nums):
            if nums[curr_idx] == prev_element:
                ele_count += 1
                curr_idx += 1
            elif nums[curr_idx] != prev_element:
                prev_ele_count = min(ele_count, 2)
                length += prev_ele_count
                while prev_ele_count > 0:
                    nums[new_arr_idx] = prev_element
                    new_arr_idx += 1
                    prev_ele_count -= 1
                prev_element = nums[curr_idx]
                ele_count = 0

        # for the last element (have no next element to compare against)
        if ele_count > 0:
            prev_ele_count = min(ele_count, 2)
            length += prev_ele_count
            while prev_ele_count > 0:
                nums[new_arr_idx] = prev_element
                new_arr_idx += 1
                prev_ele_count -= 1
        return length
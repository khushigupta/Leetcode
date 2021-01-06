class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        curr_list = []
        for num in nums:
            add = [num]
            if len(curr_list) == 0:
                curr_list = [add]
            else:
                new_list = []
                for c in curr_list:
                    new_list.append(c + add)
                curr_list += new_list
                curr_list += [add]

        curr_list.append([])
        return curr_list






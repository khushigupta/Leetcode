from collections import defaultdict


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count_dict = defaultdict(int)
        for num in nums:
            count_dict[num] += 1

        list_dict = defaultdict(list)
        for num, count in count_dict.items():
            for c in range(count):
                list_dict[num].append([num] * (c + 1))

        final_list = []

        for num, num_list in list_dict.items():
            if len(final_list) == 0:
                final_list = num_list
            else:
                new_list = []
                for l in final_list:
                    for n in num_list:
                        new_list.append(l + n)
                final_list += new_list
                final_list += num_list

        final_list.append([])

        return final_list
import sys


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        hashmap = {s: i for i, s in enumerate(list1)}
        min_sum = sys.maxint

        ans_list = list()
        for j, s in enumerate(list2):
            if s in hashmap:
                i = hashmap[s]
                min_sum = min(min_sum, i + j)

        for j, s in enumerate(list2):
            if s in hashmap:
                i = hashmap[s]
                if i + j == min_sum:
                    ans_list.append(s)

        return ans_list
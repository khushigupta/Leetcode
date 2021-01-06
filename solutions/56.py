# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def keyfunction(self, item):
        return item.start

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals

        intervals = sorted(intervals, key=self.keyfunction)

        i = 0
        j = i

        return_list = []
        curr_end = intervals[i].end

        while j < len(intervals):
            while j < len(intervals) and intervals[j].start <= curr_end:
                curr_end = max(curr_end, intervals[j].end)
                j += 1
            curr_ans = Interval(intervals[i].start, curr_end)
            return_list.append(curr_ans)
            i = j
            j = i
            if i < len(intervals):
                curr_end = intervals[i].end
        return return_list



# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        sorted_indices = sorted(range(len(intervals)), key=lambda k: intervals[k].start)
        sorted_intervals = [intervals[i] for i in sorted_indices]

        N = len(sorted_intervals)
        return_array = [-1] * N

        for i, inter in enumerate(sorted_intervals):
            # find interval with start time > end time
            pos = self.find_insert_pos(i, N - 1, inter.end, sorted_intervals)
            # position in sorted_intervals
            org_index = sorted_indices[i]
            if pos == N:
                continue
            else:
                return_array[org_index] = sorted_indices[pos]
        return return_array

    def find_insert_pos(self, low, high, target, sorted_intervals):
        while low <= high:
            mid = (low + high) // 2
            if sorted_intervals[mid].start >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low



import heapq as heap
import sys


class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # keep a min heap
        # once you're done popping k items, return that element
        nums = sorted(nums)
        H = []
        for j in range(len(nums) - 1):
            H.append((self.diff(nums[j], nums[j + 1]), j, 1))

        heap.heapify(H)
        count = 0
        while count < k:
            val, i, step = heap.heappop(H)
            if i + step + 1 < len(nums):
                step = step + 1
                heap.heappush(H, (self.diff(nums[i], nums[i + step]), i, step))
            count += 1
        return val

    def diff(self, a, b):
        return abs(a - b)
import heapq as heap


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        H = nums[:k]
        heap.heapify(H)
        for num in nums[k:]:
            min_val = heap.heappop(H)
            if num > min_val:
                heap.heappush(H, num)
            else:
                heap.heappush(H, min_val)
        return heap.heappop(H)


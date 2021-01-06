class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        N = len(nums)
        left = self.find_insert_left(0, N - 1, target, nums)
        if left == N or nums[left] != target:
            return [-1, -1]
        right = self.find_insert_right(left, N - 1, target, nums)
        return [left, right]

    def find_insert_left(self, low, high, target, nums):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def find_insert_right(self, low, high, target, nums):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return high
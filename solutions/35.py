class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return 0 if target < nums[0] else 1

        self.nums = nums
        return self.find_pos(0, len(self.nums) - 1, target)

    def find_pos(self, low, high, target):
        while low <= high:
            mid = (low + high) // 2
            if self.nums[mid] == target:
                return mid
            if self.nums[mid] > target:
                high = mid - 1
            if self.nums[mid] < target:
                low = mid + 1

        if target > self.nums[mid]:
            return mid + 1
        if target < self.nums[mid]:
            return max(mid, 0)



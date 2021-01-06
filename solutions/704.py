class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        self.nums = nums
        return self.find(0, len(nums) - 1, target)

    def find(self, low, high, target):
        while low <= high:
            mid = (low + high) // 2
            if self.nums[mid] == target:
                return mid
            if self.nums[mid] > target:
                high = mid - 1
            elif self.nums[mid] < target:
                low = mid + 1
        return -1

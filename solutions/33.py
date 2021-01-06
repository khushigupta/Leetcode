class Solution(object):
    nums = None

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 1:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        self.nums = nums
        return self.findInRotatedSortedArray(0, len(nums) - 1, target)

    def findInRotatedSortedArray(self, low, high, target):
        if high < low:
            return -1

        if high == low:
            if self.nums[low] == target:
                return low
            else:
                return -1

        mid = (low + high) / 2
        if self.nums[mid] == target:
            return mid

        # right half is sorted
        if self.nums[mid] <= self.nums[high]:
            if target >= self.nums[mid] and target <= self.nums[high]:
                return self.findInSortedArray(mid + 1, high, target)
            else:
                return self.findInRotatedSortedArray(low, mid - 1, target)

        # left half is sorted
        if self.nums[low] <= self.nums[mid]:
            if target >= self.nums[low] and target <= self.nums[mid]:
                return self.findInSortedArray(low, mid - 1, target)
            else:
                return self.findInRotatedSortedArray(mid + 1, high, target)

    def findInSortedArray(self, low, high, target):

        if high == low:
            if self.nums[low] == target:
                return low
            else:
                return -1

        if high < low:
            return -1

        mid = (low + high) / 2
        if self.nums[mid] == target:
            return mid
        if self.nums[mid] > target:
            return self.findInSortedArray(low, mid - 1, target)
        if self.nums[mid] < target:
            return self.findInSortedArray(mid + 1, high, target)

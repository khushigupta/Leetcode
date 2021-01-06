class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        N = len(nums)
        output = [1] * N
        for i in range(0, N - 1):
            output[i + 1] = output[i] * nums[i]
        prev_prod = 1
        for j in range(N - 1, -1, -1):
            curr_num = nums[j]
            nums[j] = prev_prod
            prev_prod = prev_prod * curr_num

        for i in range(N):
            output[i] *= nums[i]

        return output
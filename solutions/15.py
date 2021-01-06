# This does not do what the question demanded.
# This returns unique indices that results in a triplet.
# For example [-9, 4, 5, 5, 5, 5, 5] will return unique triplets of indices that result in 0

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.my_nums = sorted((e, i) for i, e in enumerate(nums))
        idx_set = []

        for idx, m in enumerate(self.my_nums):
            target = -1 * m[0]

            solution = self.twoSum(idx + 1, len(self.my_nums) - 1, target)
            for sol in solution:
                if len(solution) == 0:
                    continue
                idxs = [idx] + sol
                idx_set.append(idxs)

        solution_set = [[self.my_nums[i][0] for i in idx] for idx in idx_set]
        return solution_set

    def twoSum(self, begin, end, target):

        my_nums = self.my_nums

        last = len(my_nums)
        solution = []

        while begin < end:
            # print(begin, end)
            curr_sum = my_nums[begin][0] + my_nums[end][0]
            if curr_sum < target:
                begin += 1
            elif curr_sum > target:
                end = -1
            else:
                solution.append([begin, end])
                if end - 1 >= 0 and my_nums[begin][0] + my_nums[end - 1][0] == target:
                    end -= 1
                elif begin + 1 < last and my_nums[begin + 1][0] + my_nums[end][0] == target:
                    begin += 1
                else:
                    begin += 1
                    end -= 1
        return solution


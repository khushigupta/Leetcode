class Solution(object):
    mat = None

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        self.mat = matrix
        return self.find(target)

    def find(self, target):
        m = len(self.mat)
        if m == 0:
            return False
        n = len(self.mat[0])
        if n == 0:
            return False

        # find row to look for
        low = 0
        high = m - 1
        while low <= high:
            mid = (low + high) // 2
            if self.mat[mid][0] == target:
                return True
            if self.mat[mid][0] > target:
                high = mid - 1
            elif self.mat[mid][0] < target:
                low = mid + 1

        row_idx = high

        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            if self.mat[row_idx][mid] == target:
                return True
            if self.mat[row_idx][mid] > target:
                high = mid - 1
            elif self.mat[row_idx][mid] < target:
                low = mid + 1

        return False

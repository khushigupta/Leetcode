class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        M, N = len(grid), len(grid[0])

        row_max = [0 for i in range(M)]
        col_max = [0 for i in range(N)]

        for i in range(M):
            max_row = 0
            col = grid[i]
            for j in range(N):
                max_row = max(max_row, grid[i][j])
                col_max[j] = max(col_max[j], grid[i][j])
            row_max[i] = max_row

        sum = 0
        for i in range(M):
            for j in range(N):
                old_val = grid[i][j]
                grid[i][j] = min(row_max[i], col_max[j])
                sum += grid[i][j] - old_val

        return sum


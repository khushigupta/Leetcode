# https://leetcode.com/problems/maximum-length-of-repeated-subarray/submissions/
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        m = len(B)
        if n == 0 or m == 0:
            return 0

        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

        max_length = 0
        for i in range(m):
            for j in range(n):
                if B[i] == A[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_length

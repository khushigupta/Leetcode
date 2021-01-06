class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0

        b = [0 for i in range(len(A))]
        c = [0 for i in range(len(A))]

        b[0] = 1
        for i in range(1, len(A)):
            if A[i - 1] < A[i]:
                b[i] = b[i - 1] + 1
            else:
                b[i] = 1

        c[len(A) - 1] = 1
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                c[i] = c[i + 1] + 1
            else:
                c[i] = 1

        max_length = 0
        for i in range(len(A)):
            if b[i] == 1 or c[i] == 1:
                continue
            max_length = max(b[i] + c[i] - 1, max_length)
        return max_length




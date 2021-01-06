class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        N = len(s)
        if N < 2:
            return s
        if k == 1:
            return s
        s = list(s)
        if N < 2 * k:
            self.reverse(s, 0, k - 1, N)
            return ''.join(s)

        start = 0
        while start < N:
            self.reverse(s, start, start + k - 1, N)
            start = start + 2 * k
        return ''.join(s)

    def reverse(self, s, start, end, N):
        end = min(end, N - 1)
        while start < end:
            s[end], s[start] = s[start], s[end]
            end -= 1
            start += 1

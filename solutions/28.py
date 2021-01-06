class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        """
        Brute force algorithm (order N*M, in case of python, space complexity is also N)
        """
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

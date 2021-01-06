class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = 0

        idx = 0
        while idx < len(s) and s[idx] == ' ':
            idx += 1
        start = idx

        idx = len(s) - 1
        while idx > -1 and s[idx] == ' ':
            idx -= 1
        end = idx

        for i in range(end, start - 1, -1):
            if s[i] != ' ':
                length += 1
            else:
                break
        return length


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = list(s)
        countA = 0
        countL = 0
        i = 0
        while i < len(st):
            if st[i] == 'A':
                countA += 1
                i += 1
            elif st[i] == 'L':
                while i < len(st) and st[i] == 'L':
                    countL += 1
                    i += 1
                if countL > 2:
                    return False
                countL = 0
            else:
                i += 1
        return countA < 2
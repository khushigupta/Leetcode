class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == "":
            return 0

        roman = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000
                 }

        s = list(s)
        N = len(s)

        num = 0
        i = 0
        while i < N:
            if i + 1 < N and ((s[i] == 'I' and s[i + 1] == 'V') or \
                              (s[i] == 'I' and s[i + 1] == 'X') or \
                              (s[i] == 'X' and s[i + 1] == 'L') or \
                              (s[i] == 'X' and s[i + 1] == 'C') or \
                              (s[i] == 'C' and s[i + 1] == 'D') or \
                              (s[i] == 'C' and s[i + 1] == 'M')):
                num += roman[s[i + 1]] - roman[s[i]]
                i += 2
            else:
                num += roman[s[i]]
                i += 1

        return num

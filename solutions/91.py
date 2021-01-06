class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = list('abcdefghijklmnopqrstuvwxyz')
        self.num_dict = {i + 1: l for i, l in enumerate(letters)}

        s = list(s)
        s = [int(n) for n in s]

        if s[0] == 0:
            return 0

        if len(s) == 1:
            return 1

        num_ways = [0 for i in range(len(s))]
        num_ways[0] = 1

        if s[1] != 0 and s[0] * 10 + s[1] in self.num_dict:
            num_ways[1] = 2
        else:
            num_ways[1] = 1

        if len(s) == 2:
            return num_ways[1]

        for i in range(2, len(s)):
            if s[i] == 0 and self.check_hanging_zero(s[i - 1], s[i]):
                return 0
            if self.check_valid(s[i - 1], s[i]):
                num_ways[i] = num_ways[i - 1] + num_ways[i - 2]
            else:
                num_ways[i] = num_ways[i - 1]

        return num_ways[len(s) - 1]

    def check_valid(self, n1, n2):
        if n1 == 0:
            return False
        if n2 == 0:
            if n1 != 1 or n2 != 2:
        else:
            return (n1 * 10 + n2 in self.num_dict)

    def check_hanging_zero(self, n1):
        if n1 > 3 and n1 < 1:
            return True
        else:
            return False



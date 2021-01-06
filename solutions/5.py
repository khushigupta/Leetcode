class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        s = list(s)
        N = len(s)
        palindrome = [[0 for i in range(N)] for j in range(N)]

        sub_string = []
        max_len = 0

        for i in range(N):
            palindrome[i][i] = 1
            sub_string = s[i]
            max_len = 1

        for i in range(N - 1):
            if s[i] == s[i + 1]:
                palindrome[i][i + 1] = 1
                sub_string = s[i:i + 2]
                max_len = 2

        for k in range(2, N):
            for i in range(N):
                if i + k >= N:
                    continue
                if s[i] == s[i + k]:
                    palindrome[i][i + k] = palindrome[i + 1][i + k - 1]
                    if palindrome[i][i + k]:
                        if k + 1 > max_len:
                            sub_string = s[i:i + k + 1]
                            max_len = max(max_len, k + 1)
        return "".join(sub_string)

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True

        return self.is_palindrome(s, 0, len(s) - 1, 1)

    def is_palindrome(self, s, start, end, k):
        if k < 0:
            return False
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return self.is_palindrome(s, start + 1, end, k - 1) or self.is_palindrome(s, start, end - 1, k - 1)
        return True
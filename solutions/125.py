class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            else:
                while left < len(s) and not s[left].isalnum():
                    left += 1
                while right > -1 and not s[right].isalnum():
                    right -= 1
        return True
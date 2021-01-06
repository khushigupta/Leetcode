class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        if len(s) % 2:
            return False

        stack = []
        stack.append(s[0])

        for i in range(1, len(s)):
            if self.is_open(s[i]):
                stack.append(s[i])
            else:
                top = stack.pop()
                if not self.check_pair(top, s[i]):
                    return False
        if len(stack) != 0:
            return False
        return True

    def is_open(self, char):
        if char == '{' or char == '[' or char == '(':
            return True
        return False

    def check_pair(self, open, close):
        if open == '{' and close == '}':
            return True
        if open == '[' and close == ']':
            return True
        if open == '(' and close == ')':
            return True
        return False

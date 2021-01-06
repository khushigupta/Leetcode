class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.wordDict = wordDict

        if s is None or s == "":
            return False
        return self.check(s)

    def check(self, word):

        if word in self.wordDict:
            return True

        N = len(word)
        for i in range(1, N):
            if self.check(word[:i]) and self.check(word[i:]):
                return True
        return False

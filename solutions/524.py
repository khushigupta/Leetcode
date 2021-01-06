class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        if s == "":
            return ""

        string = list(s)
        self.alpha = {v: 1 for v in string}

        max_len = 0
        result = ""

        for w in d:
            word = list(w)
            if not self.compare(string, word):
                continue

            if len(word) > max_len:
                max_len = len(word)
                result = ''.join(word)
            elif len(word) == max_len:
                this_str = ''.join(word)
                if this_str < result:
                    result = this_str
        return result

    def compare(self, string, word):
        for w in word:
            if w not in self.alpha:
                return False
        i = 0
        j = 0
        while i < len(string) and j < len(word):
            if string[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(word)
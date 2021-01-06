from collections import defaultdict


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        mdict = defaultdict(int)
        for m in magazine:
            mdict[m] += 1

        ransom = list(ransomNote)
        for r in ransom:
            if r not in mdict:
                return False
            available = mdict[r]
            if available <= 0:
                return False
            mdict[r] = mdict[r] - 1

        return True
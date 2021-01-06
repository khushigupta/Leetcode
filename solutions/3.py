from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0

        count_dict = defaultdict(int)
        max_len = 0
        while r < len(s):
            char = s[r]
            count_dict[char] += 1
            # contract
            while l <= r and count_dict[char] > 1:
                char_remove = s[l]
                count_dict[char_remove] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            # expand
            r += 1
        return max_len



